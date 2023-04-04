from market import app
from flask import render_template

from market.forms import LoginForm


@app.route('/')
@app.route('/home')
def home_page():

    return render_template('home.html')

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',form=form)

@app.route('/catalogo')
def catalogo():

    return render_template('catalogo.html')