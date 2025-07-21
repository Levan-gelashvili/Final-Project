from flask import Flask, render_template, redirect, url_for, request, session, abort
from forms import RegisterForm, LoginForm, PodcastForm, NewsForm
from werkzeug.utils import secure_filename
from models import User, Podcast, News
from ext import app, db
from PIL import Image
import os


@app.route("/")

def home():
    return render_template("home.html")


@app.route("/news", methods=['GET', 'POST'])
def news():
    form = NewsForm()
    news_list = News.query.all()

    if 'username' not in session:
        return render_template("news.html", news_list=news_list, form=None, user_role=None)

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        image_file = form.image.data

        filename = secure_filename(image_file.filename)
        image_path = os.path.join(app.root_path, 'static/images', filename)
        image_file.save(image_path)

        new_news = News(
            title=title,
            content=content,
            image=filename
        )

        db.session.add(new_news)
        db.session.commit()

        return redirect(url_for('news'))

    return render_template("news.html", news_list=news_list, form=form, user_role=session.get('role'))

def admin_required():
    if session.get('role') != 'admin':
        abort(403)

@app.route('/news/delete/<int:news_id>', methods=['POST'])
def delete_news(news_id):
    if session.get('role') != 'admin':
        abort(403)
    news = News.query.get_or_404(news_id)
    db.session.delete(news)
    db.session.commit()
    return redirect(url_for('news'))

@app.route('/news/<int:news_id>')
def news_detail(news_id):
    news = News.query.get_or_404(news_id)
    return render_template('detailed.html', news=news, user_role=session.get('role'))

@app.route("/about")

def about():
    return render_template("abt.html")



def admin_required():
    if session.get('role') != 'admin':
        abort(403)  # Forbidden

@app.route("/podcasts", methods=['GET', 'POST'])
def podcasts():
    if 'username' not in session:
        return redirect(url_for('login'))

    form = PodcastForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        video_url = form.video_url.data
        image_file = form.image.data

        filename = secure_filename(image_file.filename)
        image_path = os.path.join(app.root_path, 'static/images', filename)
        image_file.save(image_path)

        with Image.open(image_path) as img:
            width, height = img.size
            min_dim = min(width, height)
            left = (width - min_dim) / 2
            top = (height - min_dim) / 2
            right = (width + min_dim) / 2
            bottom = (height + min_dim) / 2
            img_cropped = img.crop((left, top, right, bottom))
            img_cropped.save(image_path)

        new_podcast = Podcast(
            title=title,
            description=description,
            video_url=video_url,
            image=filename
        )
        db.session.add(new_podcast)
        db.session.commit()
        return redirect(url_for('podcasts'))

    podcasts = Podcast.query.all()
    return render_template("pd&int.html", podcasts=podcasts, form=form, user_role=session.get('role'))


@app.route('/podcasts/delete/<int:podcast_id>', methods=['POST'])
def delete_podcast(podcast_id):
    admin_required()
    podcast = Podcast.query.get_or_404(podcast_id)
    db.session.delete(podcast)
    db.session.commit()
    return redirect(url_for('podcasts'))




@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    message = ""

    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            message = "Username already exists."
        else:
            new_user = User(
                username=form.username.data,
                password=form.password.data,
                birthday=str(form.birthday.data),
                country=form.country.data
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))

    return render_template("register.html", form=form, message=message)




@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    message = ""
    user = None

    if request.method == "POST":
        if form.validate():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.password == form.password.data:  # later: use hashed passwords!
                session['username'] = user.username
                session['birthday'] = user.birthday
                session['country'] = user.country
                session['role'] = user.role  # <-- Add this line

                return redirect(url_for('home'))
            else:
                message = "Invalid credentials."
        else:
            message = "Please fix the form errors."
    return render_template("login.html", form=form, message=message)



@app.route('/logout')
def logout():
    session.pop('username', None) 
    return redirect(url_for('home'))
