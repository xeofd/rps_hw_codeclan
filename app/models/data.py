from app.models.classes import Player, Game
# Create data for the app

computer = Player('computer', 'rock')

players = [computer]

def add_player(player):
    players.append(player)

def start_new_game():
    new_game = Game()
    return new_game

def remove_player():
    players.pop(1)