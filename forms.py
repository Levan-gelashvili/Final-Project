from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange, URL
from flask_wtf.file import FileAllowed, FileRequired

class RegisterForm(FlaskForm):
    username = StringField("Create Username", validators=[DataRequired()])
    password = PasswordField("Create Password", validators=[DataRequired(), Length(min=8, max=20)])
    repeat_password = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password", message="Passwords must match")])
    birthday = IntegerField("Select Your Birth Year", validators=[DataRequired(), NumberRange(min=1900, max=2025, message="Enter a valid year")])
    country = SelectField(
        choices=[
            ('', 'Select Your Country'),
            ('', 'Select Your Country'),
        ('United States', 'United States'),
        ('United Kingdom', 'United Kingdom'),
        ('Germany', 'Germany'),
        ('France', 'France'),
        ('Italy', 'Italy'),
        ('Japan', 'Japan'),
        ('South Korea', 'South Korea'),
        ('China', 'China'),
        ('Russia', 'Russia'),
        ('India', 'India'),
        ('Brazil', 'Brazil'),
        ('Canada', 'Canada'),
        ('Australia', 'Australia'),
        ('Spain', 'Spain'),
        ('Mexico', 'Mexico'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('Turkey', 'Turkey'),
        ('Argentina', 'Argentina'),
        ('Netherlands', 'Netherlands'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Georgia', 'Georgia'),
        ('Estonia', 'Estonia'),
        ('Slovenia', 'Slovenia'),
        ('Croatia', 'Croatia'),
        ('Lithuania', 'Lithuania'),
        ('Latvia', 'Latvia'),
        ('Armenia', 'Armenia'),
        ('Portugal', 'Portugal'),
        ('New Zealand', 'New Zealand'),
        ('Czech Republic', 'Czech Republic'),
        ('Finland', 'Finland'),
        ('Norway', 'Norway')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()

class PodcastForm(FlaskForm):
    title = StringField('Podcast Title', validators=[DataRequired()])
    description = TextAreaField('Podcast Description', validators=[DataRequired(), Length(min=10, max=500, message="Description must be between 10 to 500 characters.")])
    video_url = StringField('Video URL', validators=[DataRequired(), URL()])
    image = FileField('Podcast Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')
    ],  render_kw={"class": "file-input"})

class NewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=22)])
    content = TextAreaField('Content', validators=[DataRequired()])
    image = FileField('Image', validators=[DataRequired(), NumberRange(min=1900, max=2025)])