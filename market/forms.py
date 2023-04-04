from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired
class LoginForm(FlaskForm):
    email = StringField(label='E-mail:')
    password = PasswordField(label='Contraseña:')
    submit = SubmitField(label='Iniciar sesión')

class RegisterForm(FlaskForm):
    email = StringField(label='E-mail:')
    username = StringField(label='Nombre de usuario:')
    password1 = PasswordField(label='Contraseña:')
    password2 = PasswordField(label='Confirmar contraseña:')
    submit = SubmitField(label='Crear cuenta')