# Name:
# Section:
# strings_and_lists.py

print "\n**********  Exercise 4.1 **********"
def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num
    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])


def cumulative_sum(number_list):
    cumulative_list = [number_list[0]]
    for x,num in enumerate(number_list[1:]):
        cumulative_list.append(num + cumulative_list[x])
    return cumulative_list


# Test Cases
numlist1 = [3,4,5,6,2,1,2]
numlist2 = [1,2,3,4,5]
print "\nCumulative lists"
print cumulative_sum(numlist1)
print cumulative_sum(numlist2)

# **********  Exercise 4.2 **********

# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    if word[0].isalpha():
        if word.startswith(tuple(VOWELS)):
            word += "hay"
        else:
            word = word[1:] + word[0] + "ay"
        return word  
    else:
        error = "Error: The word does not start with a letter"
        return error
# Test Cases
print pig_latin("boot")
print pig_latin("image")

# **********  HW 2 complete! *********
