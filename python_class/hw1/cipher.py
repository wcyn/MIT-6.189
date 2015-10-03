# Name: Cynthia Wasonga
# Date: 3rd October 2015
# zellers.py

print "\n********** Exercise OPT.2 - Secret Messages **********"

def prompt_user():
	shift = False
	phrase = raw_input("Enter a phrase to encode: ")
	while not shift:
		try:
			shift = int(raw_input("Enter the shift value: "))
		except ValueError:
			print "Please enter an integer"
	return [phrase,shift]

def encode_phrase(phrase, shift):
	#65{A} 90{Z} to 97{a} 122{z}

	encoded_phrase = [ord(a) for a in phrase]
	for i,num in enumerate(encoded_phrase):
		if chr(num).isalpha():
			encoded_phrase[i]+=shift
			if encoded_phrase[i] > ord('z') and chr(num).islower():
				# This caters for overly high shift values
				encoded_phrase[i] = ord('a') + ((encoded_phrase[i] % ord('z')) - 1) % 26 #26 letters of alphabet.
			elif encoded_phrase[i] > ord('Z') and chr(num).isupper():
				encoded_phrase[i] = ord('A') + ((encoded_phrase[i] % ord('Z')) - 1) % 26

	decoded = [chr(c) for c in encoded_phrase]
	return decoded
	
#TEST CASES
phrase, shift = prompt_user()
print "\n","".join(encode_phrase(phrase,shift))

phrase = "Mayday! Mayday!"
shift = 4
print "\n","".join(encode_phrase(phrase,shift)) #output: Qechec! Qechec!


phrase = "MaYdaY!! MaYday!@#"
shift = 4
print "\n","".join(encode_phrase(phrase,shift)) #output: QeCheC!! QeChec!@#

phrase = "mayday!! mayday!!"
shift = 108
print "\n","".join(encode_phrase(phrase,shift)) #output: quechec!! quechec!!





