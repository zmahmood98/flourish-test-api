from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

from flourish_app.models import Users

class RegisterForm(FlaskForm):
    username = StringField(validators = [InputRequired(), Length(
        min = 4, max = 64)], render_kw = {"placeholder": "Username"})

    password = PasswordField(validators = [InputRequired(), Length(
        min = 4, max = 25)], render_kw = {"placeholder": "Password"})

    submit = SubmitField("Register")    
    def validate_username(self,username):
       existing_user = Users.query.filter_by(username=username.data).first()
       if existing_user:
           raise ValidationError("That username already exists")

class LoginForm(FlaskForm):
    username = StringField(validators = [InputRequired(), Length(
        min = 4, max = 64)], render_kw = {"placeholder": "Username"})

    password = PasswordField(validators = [InputRequired(), Length(
        min = 4, max = 25)], render_kw = {"placeholder": "Password"})
    submit = SubmitField("Login")
