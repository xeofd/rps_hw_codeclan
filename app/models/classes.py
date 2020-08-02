# New Class: Player
# Creates a player that will chose a position in Rock/Paper/Scisors
# which will then be compaired to the computers position.

class Player:
    def __init__(self, player_name, player_choice):
        self.name = player_name
        self.choice = player_choice

# New Class: Game
# Create a game class which will take in two Player classes and compare
# their choices to generate a winner && loser

class Game:
    def __init__(self):
        self.players = []

    # class function
    def add_players_to_game(self, player):
        self.players.append(player)

    def win_check(self):
        pass