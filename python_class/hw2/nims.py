# Name: Cynthia Wasonga
# Date: 1st October 2015
# nims.py
def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''
    player1 = "Player 1"
    player2 = "Player 2"
    d = {player1:player2,player2:player1}
    player_name = player1
    
    while True:
		pl_num = raw_input(player_name+": Number of stones? ")
		try: 
			pl_int = int(pl_num)
			# print "max_stones: ", max_stones
			if pl_int > max_stones:
				print "You have entered more stones than is allowed"
			elif pl_int == pile:
				print player_name, "wins!"
				return 
			elif pl_int > pile:
				print "Not enough stones left"
				player_name = d[player_name] #can comment this to maintain current player
			else:
				print "pile before: ", pile
				pile -= pl_int
				player_name = d[player_name] #toggle player
				print "pile after: ", pile
		except ValueError:
			print "Error. Please enter a number"
				
play_nims(10,3)