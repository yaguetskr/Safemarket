from flask import Flask, render_template



app = Flask(__name__)
app.config['SECRET_KEY'] = 'seguridadufvaslkofja'

from market import routes