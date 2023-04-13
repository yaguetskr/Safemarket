
from wtforms import StringField, PasswordField, SubmitField, Form
from wtforms.validators import Length, EqualTo, Email, DataRequired
class LoginForm(Form):
    username = StringField(id='username',label='Nombre de usuario:')
    pwd = PasswordField(id='pwd',label='Contraseña:')
    submit = SubmitField(id='submit',label='Iniciar sesión')

class RegisterForm(Form):
    email = StringField(id='email',label='E-mail:')
    username = StringField(id='username',label='Nombre de usuario:')
    password1 = PasswordField(id='pwd',label='Contraseña:')
    password2 = PasswordField(id='pwd2',label='Confirmar contraseña:')
    submit = SubmitField(id='submit',label='Crear cuenta')