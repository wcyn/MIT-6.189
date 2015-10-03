# Name: Cynthia Wasonga
# Date: 30th September 2015
# homework_1.py

##### Template for Homework 1, exercises 1.2-1.4 ######

print "********** Exercise 1.2 (Tic-Tac-Toe) **********"
for x in range(2):
	print " "*2 + "|" + " "*2 + "|"
	print "-"*8 
print " "*2 + "|" + " "*2 + "|\n" 

print "********** Exercise 1.3 (Tic-Tac-Toe Vars)**********"

# Do your work for Excercise 1.3 here. Hint - how many different
# variables will you need?
#Answer: 3 Variables
space = " " * 2
pipe = "|"
dash = "-"

for x in range(2):
	print space + pipe + space + pipe 
	print dash * 8 
print space + pipe + space + pipe + "\n"


print "********** Exercise 1.4 **********"

fname = raw_input("Enter your first name: ")
lname = raw_input("Enter your last name: ")
print "Enter you date of birth:"
month = raw_input("Month? ")
day	= raw_input("Day? ")
year = raw_input("Year? ")

print fname, lname, "was born on", month, day+",", year
