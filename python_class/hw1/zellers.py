# Name: Cynthia Wasonga
# Date: 3rd October 2015
# zellers.py

MONTHS = {
			"march":1, "april":2, "may":3,
			"june":4, "july":5, "august":6,
			"september":7, "october":8, "november":9,
			"december":10, "january":11, "february":12
		}
MONTH_30 = [2,4,7,9]
MONTH_31 = [11,1,3,5,6,8,10]
DAYS = {
		0:"sunday", 1:"monday", 2:"tuesday", 3:"wednesday",
		4:"thursday", 5:"friday", 6:"saturday"
		}

print "\n********** Exercise OPT.1 - Zellers Algorithm **********"
print "Enter the following details about a certain date and find out the day"
def ask_user():
	A,C,B,D = [False,False,False,False] #Multiple assignments

	while not (A and C and D):
		try:
			if not A:
				month = (raw_input("Month? ")).lower()
				A = MONTHS[month]
			while not B: #handle number of days for specific months
				B = int(raw_input("\nDate of the Month? "))
				if (A in MONTH_30 and B > 30) or (A in MONTH_31 and B > 31) \
					or (A == 12 and B > 29 ): 
					print "You have entered more days than there are in",month.title()
					B = False

			if not C:C = int(raw_input("\nYear of the Century eg. 98 for 1998? "))
			if not D:D = int(raw_input("\nCentury eg. 19 for year 1998?"))
			
		except KeyError:
			print "Error: That month is not a valid month"
		except ValueError:
			print "Please Enter an integer"
	return [A,B,C,D]

	# print A, B, C, D
A,B,C,D = ask_user()
def calculate_day(A,B,C,D):
	W = (13*A - 1) / 5
	X = C / 4
	Y = D / 4
	Z = W + X + Y + B + C - 2*D
	R = Z % 7
	return DAYS[R].title()

print "\nThe day for that date is",calculate_day(A,B,C,D)


