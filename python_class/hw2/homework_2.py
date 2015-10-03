# Name: Cynthia Wasonga
# Date: 1st October 2015
# Section:
# homework_2.py
import math
import rps 
import random
##### Template for Homework 2, exercises 3.1-3.4  ######
print "\n**********  Exercise 2.1 **********"
# player1 = rps.ask("Player1")
# player2 = rps.ask("Player2")
# rps.result(player1,player2)

print "\n**********  Exercise 3.1 **********" 
# Define your rock paper scissors function here

pl1wins = [("rock", "scissors"), 
		("paper", "rock"),
		("scissors", "paper"), ]

def rpsgame((pl1, opt1), (pl2, opt2)):
	if ((opt1, opt2)) in pl1wins:
		return pl1
	elif opt1 == opt2:
		return "It's a Tie!"
	else:
		return pl2

# Test Cases for Exercise 3.1

print "Winner?", rpsgame(("Mary","paper"),("Claire","paper"))
print "Winner?", rpsgame(("John","rock"),("Steve","scissors"))
print "Winner?", rpsgame(("Hillary","paper"),("Alex","rock"))
print "Winner?", rpsgame(("Sarah","scissors"),("Pat","paper"))


print "\n*********** Exercise 3.2 ***********"
## 1 - multadd function
def multadd(a,b,c):
	return a*b+c

print "\nmultadd(2,3,4): ", multadd(2,3,4)

## 2 - Equations

angle_test = math.sin(math.pi/4) +\
 math.cos(math.pi/4)/2

print "\nsin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test = math.ceil(276/19.0) + (2 * math.log(12,7))
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test

## 3 - yikes function
def yikes(num):
	return multadd(num,math.pow(math.e,-num),math.sqrt(1-math.pow(math.e,-num)))

# Test Cases
x = 5
print "yikes(5) =", yikes(x)

print "\n********** Exercise 3.3 **********"

def rand_divis_3():
	num = random.randint(0,100)
	print num, "divisible by 3?"
	if num % 3 == 0 and num != 0: 
		return True
	else: 
		return False
print rand_divis_3()

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
def roll_dice(num1, num2):
	for x in range(0, num2):
		roll = random.randint(1,num1)
		print roll
	print "That's all"


# Test Cases
print "\nRolling Dice..."
roll_dice(6,3)                          

