from flask import Flask, render_template



app = Flask(__name__)
app.config['SECRET_KEY'] = 'una_cadena_aleatoria_y_segura'

from market import routes