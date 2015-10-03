# Name: Cynthia Wasonga
# Date: 2nd October 2015
# list_comp.py

print "\n ********** OPT.2.1 **********"
def ints_in_list(somelist):
	return [x for x in somelist if isinstance(x, int)]

# Test Cases
alist = ['hello', 3, 5.4, "again", 1]
print ints_in_list(alist)

print "\n ********** OPT.2.2 **********"
x = [i for i in range(-5,6)]
y = [i for i in range(0,11)]

print "\t---Linear Equation pairs---"
print [[i, i**2+1] for i in x if i**2+1 in y ]

print "\n ********** OPT.2.3 **********"
#equation (x-a)^2 + (y-b)^2 = r^2 where (a,b) are the center coordinates
#let a = b = 0 i.e center => (0,0)
#Thus x^2 + y^2 = r^2; y^2 = r^2 - x^2

r = 5 #radius
print "\t---Circle Equation pairs---"
print [[i, r**2 - i**2] for i in x if r**2 - i**2 in y ]
