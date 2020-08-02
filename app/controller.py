# Import functions and classes
from flask import render_template, request, redirect
from app import app
from app.models.classes import Player, Game
from app.models.data import players, add_player, start_new_game, remove_player

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    # check for and remove old players
    if len(players) > 2:
        remove_player()
    # start new game, create new player, add player to list
    current_game = start_new_game()
    # add computer and new player to game
    for player in players:
        current_game.add_players_to_game(player)

    # check there are enough players to run the winner check
    if (len(current_game.players) == 2):
        winner_found =  current_game.win_check()
    else: 
        winner_found = 'Start a game to get a winner'
    return render_template('game.html', winner_found=winner_found)

@app.route('/game/data', methods=['POST'])
def game_data():
    name = request.form['player_name']
    choice = request.form['player_choice']
    new_player = Player(name, choice)
    add_player(new_player)
    return redirect('/game')