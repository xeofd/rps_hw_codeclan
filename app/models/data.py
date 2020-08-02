from app.models.classes import Player
# Create data for the app

computer = Player('computer', 'rock')

players = [computer]

def add_player(player):
    players.append(player)