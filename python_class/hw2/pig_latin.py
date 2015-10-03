# Name: Cynthia Wasonga
# Date: 1st October 2015
# pig_latin.py
import re #regex
VOWELS = ['a', 'e', 'i', 'o', 'u']
SPECIAL = ['th', 'st', 'qu', 'pl', 'tr']
PUNCTUATION = [',', '.', '!', ':', ';']

def pig_latin(word):
    punc = []
    word = word.lower() # convert to lowercase
    for letter in word:
        if letter in PUNCTUATION:
            punc.append(letter)
            word = word.replace(letter,'')
            print punc

    if word[0].isalpha():
        if word.startswith(tuple(VOWELS)):
            word += "hay" + "".join(punc)
        elif word.startswith(tuple(SPECIAL)):
            word = word[2:] + word[:2] + "ay" + "".join(punc)
        else:
            word = word[1:] + word[0] + "ay"
        return word + "".join(punc) 
    else:
        error = "Error: The word does not start with a letter"
        return error

# Test Cases
print pig_latin("boot")
print pig_latin("im;.age")
print pig_latin("st,o.p")
print pig_latin("there:")


