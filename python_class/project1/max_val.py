# Name: Cynthia Wasonga
# Date: 2nd October 2015
# max_val.py

print "\n**********  Project 1.1 **********" 
def all_less_than(some_list, num):
	for x in some_list:
		if x >= num: return False
	return True

def one_less_than(some_list, num):
	for x in some_list:
		if x < num: return True
	return False

#Test Cases
my_list1 = [1,2,3,4,5] 
my_list2 = [7,8,9,6] 

print all_less_than(my_list1,6) #True
print all_less_than(my_list2,6) #False

print one_less_than(my_list1,6) #True
print one_less_than(my_list2,6) #False


