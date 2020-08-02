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
        # set the players choices
        p1 = self.players[0].choice
        p2 = self.players[1].choice

        # run the check
        if (p1 == p2):
            return 'DRAW'
        elif (p1 == 'paper' and p2 == 'rock'):
            return self.players[0].name
        elif (p1 == 'rock' and p2 == 'scissors'):
            return self.players[0].name
        elif (p1 == 'scissors' and p2 == 'paper'):
            return self.players[0].name
            
        elif (p2 == 'paper' and p1 == 'rock'):
            return self.players[1].name
        elif (p2 == 'rock' and p1 == 'scissors'):
            return self.players[1].name
        elif (p2 == 'scissors' and p1 == 'paper'):
            return self.players[1].name