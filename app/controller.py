# Import functions and classes
from flask import render_template, request, redirect
from app import app
from app.models.classes import Player, Game
from app.models.data import players, add_player, start_new_game

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/<name>/<choice>')
def game(name, choice):
    # start new game, create new player, add player to list
    current_game = start_new_game()
    new_player = Player(name, choice)
    add_player(new_player)
    # add computer and new player to game
    for player in players:
        current_game.add_players_to_game(player)

    winner_found =  current_game.players[0].name
    return render_template('game.html', winner_found=winner_found)