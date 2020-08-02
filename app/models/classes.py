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
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    # class function
    def win_check(self):
        vs1 = self.player_1.choice
        vs2 = self.player_2.choice
        if (vs1 == 'rock' and vs2 == 'scissors'):
            return self.player_1.name
        elif (vs1 == 'scissors' and vs2 == 'paper'):
            return self.player_1.name
        elif (vs1 == 'paper' and vs2 == 'rock'):
            return self.player_1.name
        elif (vs2 == 'rock' and vs1 == 'scissors'):
            return self.player_1.name
        elif (vs2 == 'scissors' and vs1 == 'paper'):
            return self.player_1.name
        elif (vs2 == 'paper' and vs1 == 'rock'):
            return self.player_1.name