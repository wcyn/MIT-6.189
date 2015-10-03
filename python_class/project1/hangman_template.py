# Name: Cynthia Wasonga
# Date: 2nd October 2015
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
import sys
from random import randrange
from hangman_lib import *
from string import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' # Change this 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    # if letters in secret_word contained in letters_guessed
    if set(secret_word).issubset(set(letters_guessed)):
        return True
    return False

    """Alternatively..."""
    # for i in secret_word:
    #     if i not in letters_guessed:
    #         return False
    # return True

def print_guessed():
    '''
    Returns a string that contains the word with a dash "-" in
    place of letters not guessed yet. 
    '''
    global secret_word
    global letters_guessed

    #elements in secret word that are not in letters_guessed
    missing =  set(secret_word) - set(letters_guessed)
    # print missing

    for i in secret_word:
        if i in missing:
            sys.stdout.write("_") # to avoid newline that comes with print fn
        else:
            sys.stdout.write(i)
    print "\n" #newline

    print "Letters not guessed yet:"
    print [a for a in ascii_lowercase if a not in letters_guessed]
    
def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()

    while True:
        print_hangman_image(mistakes_made)
        guesses_left =  MAX_GUESSES - mistakes_made
        print guesses_left,"guesses left"

        if guesses_left < 1:
            print_guessed()
            print "Sorry :( You Lost."
            print "The word was: ", secret_word
            break

        print_guessed()

        letter = raw_input("Enter a letter or the word 'guess' to guess the whole word: ").lower()
        if letter == 'guess':
            whole_word = raw_input("Enter the whole word: ").lower()
            if whole_word == ''.join(secret_word):
                print "\nYou Won!!"
                print secret_word
                break
            else:
                mistakes_made += 2
                print "Woops! You're speeding up your death :\\"


        if letter in letters_guessed:
            print "\nLetter has already been guessed"
        else:
            letters_guessed.append(letter)
            if letter in secret_word:
                print "\nGreat!"
                # print_guessed()
            else:
                print "\nOh, No!"
                mistakes_made += 1
                # print_guessed()
        if word_guessed():
            print "\nYou Won!!"
            print secret_word
            break


play_hangman()


    
