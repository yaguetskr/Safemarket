

from market import app
from flask import render_template, request, redirect, url_for, session, make_response

from market.forms import *
from market.petitions import *


@app.route('/')
@app.route('/home')
def home_page():

    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()

    if request.method=='POST':
        # procesar los datos del formulario
        user = request.form['username']
        password = request.form['pwd']
        cookie=loginpetition(user,password)

        if cookie:
            print(cookie.content)
            print('prueba2')
            print(cookie.content)
            response = make_response('Inicio de sesión exitoso!')
            response.set_cookie('session_token', cookie.content)
    return render_template('login.html',form=form)


@app.route('/catalogo')
def catalogo():
    products=getproducts()
    return render_template('catalogo.html',products=products)