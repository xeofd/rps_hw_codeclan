# Import functions and classes
from flask import render_template, request, redirect
from app import app
from app.models.classes import Player, Game
from app.models.data import players, add_player

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    pass