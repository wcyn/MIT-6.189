# Pl1		Pl2		Result
#--------------------------
# Rock		Rock		Tie
# Rock		Scissors	Pl1
# Rock		Paper		Pl2
# Paper		Rock		Pl1
# Paper		Paper		Tie
# Paper		Scissors	Pl2
# Scissors	Rock		Pl2
# Scissors	Paper		Pl1
# Scissors	Scissors	Tie

valid = ["rock", "paper", "scissors"] #Valid objects
#Conditions for Player 1 wins
p1wins = [("rock", "scissors"), 
		("paper", "rock"),
		("scissors", "paper"), ]

def ask(player_name):
	while True:
		player = raw_input(player_name+"? ")
		plower = player.lower()
		if plower not in valid:
			print "This is not a valid objet selection "
		else:
			return plower

def result(pl1, pl2):
	if ((pl1, pl2)) in p1wins:
		print "Player 1 wins"
	elif pl1 == pl2:
		print "It's a Tie"
	else:
		print "Player 2 wins"

# allows this module to be used as a library
if __name__ == "__main__":
	print "------- Rock, Paper, Scissors -------"
	player1 = ask("Player1") 
	player2 = ask("Player2")
	result(player1,player2)
	