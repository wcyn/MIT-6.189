# Name: Cynthia Wasonga
# Date: 2nd October 2015
# homework_3.py


##### Template for Homework 3, exercises 5.1 - 5.5 ######
import math, os, re

print "\n**********  Exercise 5.1 **********" 
print "Documentation done on homework_3.py file"

"""corrections slotted in the functions as comments"""

def negate(num):
    return -num

def large_num(num):
    res = (num > 10000)
    # return res

# Bugs
##### BUG 1 #####
# negate(b)
# neg_b = num
# print 'b:',b,'neg_b',neg_b

# big = large_num(b)
# print 'b is big:', big

"""
BUG 1
------
variable b is not defined before passing it 
on as an argument

variable num is also not defined before 
assigning it to neg_b
"""

##### BUG 2 #####
"""
BUG 2
------
The function large_num does not return any
value and thus cannot be utilized

"""
# print large_num(10001) #returns None
##### BUG 3 #####
"""
BUG 3
------
The two functions do not handle inputs other than 
numerics properly. The errors are not caught.

"""
# print large_num("j")
# print negate("hi")

print "\n**********  Exercise 5.2 **********" 

# Define "Mutable" and list what data structures have this characteristic
"""
Mutable objets are objects whose values can be changed.
Mutable types can be changed in place
A list of Mutable data srtuctures include:
1. Lists
2. Dictionaries
3. Sets
4. Byte array
"""
#E+xample 1
y = [1,2,3] 
x = y
x.append(5)
print y #outputs [1,2,3,5]

# Define "Immutable" and list what data structures have this characteristic
"""
Immutable objets are objects whose values cannot be changed.
Immutable types cannot be changed in place.
A list of Immutable data srtuctures include:
1. Tuples
2. Strings
3. Bytes
4. Integer, Floats, Long
5. Frozen Sets
"""

#Example 2
y = "hey"
x = y
x += " there"
print y #outputs hey

# **********  Exercise 5.3 **********

def ball_collide(ball1, ball2):
    '''
    Computes whether or not two balls are colliding
    
    ball1: a tuple of (x-coord, y-coord, radius) nums (ints or floats);
        represents first ball
    ball2: a tuple of (x-coord, y-coord, radius) nums (ints or floats); 
        represents second ball

    returns: True if the balls collide and False if they do not collide
    '''
    dist = math.sqrt((ball1[0]-ball2[0])**2 + (ball1[1]-ball2[1])**2 )
    if dist <= ball1[2] + ball2[2]:
        return True
    return False    
    

# Test Cases for Exercise 5.3
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True


print "\n********** Exercise 5.4 **********"

def add_class(class_num, desc, class_dict):
    '''
    Adds a class number/class name pair to a dictionary
    
    class_num: a string; the MIT number associated with the class
    desc: a string; the English name of the class
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; only modifies class_dict
    '''
    class_dict.update({class_num:desc})

def print_classes(course, class_dict):
    '''
    Prints out all the classes you've taken in a given Course.
     If no classes were taken in the Course, print out that none were taken
    
    course: a string; the Course for which we would like to
     print out classes taken
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; simply prints out relevant information
    '''

    courses = False

    try:
        courses = {key:class_dict[key] for key in class_dict if key.startswith(course)}
        
        if courses:
            for key,val in courses.items():
                print key,"-",val
        else:
            print "No Course",course,"classes taken"
    except TypeError:
        print "Error - The course shoud be a string"

# Test Cases for Exercise 5.4
my_classes = {"101":"Introduction to Programming",
                "102":"Computer Systems",
                "103":"Algorithms",
                "201":"Algebra",                "6.s189":"Introduction to Python",
                "6.01":"Introduction to EECS"
                }

print_classes("1",my_classes)
print_classes(6,my_classes) #gives an error

print "\n********** Exercise 5.5 **********"

def buildAddrBook(fileName):
    '''
    Builds an address book from a file.
    
    fileName: a string, the name of the file to read in
     File must be in the format specified in Exercise 5.5.

    returns: a dictionary with keys and values generated
      from the file, as specified in Exercise 5.5.
    '''
    if not os.path.exists(fileName):
        print "Error: File, '%s' does not exist" %fileName
        return
    if fileName.lower().endswith(".csv"):
        with open(fileName,"r") as f:
            try:
                return {", ".join(line.split(",")[:2]):line.split(",")[2:] for line in f}
            except IOError:
                print "Error: Could not open file: '%s'" %fileName
    else:
        print "Error: The input file must be a csv file"
        

def changeEntry(addrBook, entry, field, newValue, newEntry=False):
    '''
    Changes one entry in the specified address book.

    addrBook: a dictionary in the address book format
      returned by buildAddrBook.
    entry: a string; the pre-existing entry to change
    field: a string; the field to change (one of: "name",
      "phoneNumber", "emailAddress")
    newValue: the new value for the specified field

    returns: nothing; only modifies addrBook
    '''
    VALID_FIELDS = ['name', 'phoneNumber', 'emailAddress']
    
    if isinstance(addrBook, dict):
        if field not in VALID_FIELDS:
            print "Error: The only valid fields are: ",", ".join(VALID_FIELDS)
            return

        if entry in addressBook.keys():
            if newEntry:
                print "Entry '%s' already exists."%entry
                return
            if field == "name":           
                addressBook[newValue] = addressBook.pop(entry) #change key value
            elif field == "phoneNumber" :
                addressBook[entry][0] = newValue
            elif field == "emailAddress":
                if re.match(r'^[\w.-]+@[\w.-]+\.[\w-]+$', newValue, re.I): #check if email address is valid
                    addressBook[entry].append(newValue)

                else: 
                    print "Error: Invalid email address '%s'" %newValue
        
        elif newEntry:
            addressBook[entry] = [""] 
            if field == "name": 
                print "'newValue' field ignored. Using entry as name."
            elif field == "phoneNumber" :
                addressBook[newEntry][0] = newValue
            elif field == "emailAddress":
                if re.match(r'^[\w.-]+@[\w.-]+\.[\w-]+$', newValue, re.I): #check if email address is valid
                    addressBook[entry].append(newValue)

                else: 
                    print "Error: Invalid email address '%s'" %newValue
        else:
            print "Error: The entry '%s' does not exist" %entry
    else:
        print "Error: The address book must be a dictionary"

# Test Cases for Exercise 5.5
addressBook = buildAddrBook("rawAddresses.csv")
buildAddrBook("rawAddreses.csv")
buildAddrBook("homework_3.pdf")

changeEntry(addressBook,"Beaver, Tim","emailAddress","beaver.tim@d.c.h.l")
changeEntry(addressBook,"Nadal, Rafael","emailAddress","beaver.tim@d.") #gives an error msg
changeEntry(addressBook,"Nadal, Rafael","phoneNumber","07-342122")
changeEntry(addressBook,"Manchu, Foo","name","Manchu, Someone")

#add new entries?
changeEntry(addressBook,"Manchu, Foo","name","Manchu, Someone", True)
changeEntry(addressBook,"Cynthia, Wasonga","emailAddress","w.c@g.c", True)
changeEntry(addressBook,"Cynthia, Wasonga","phoneNumber","324-242", False)
changeEntry(addressBook,"Cynthia, Wasonga","emailAddress","was.c@gmail.c", False)

print "\n"+"-"*8 + "Address Book " + "-"*8

#view changes
i = 1
for k,v in addressBook.items():
    print i,":",k,"-",v 
    i+=1