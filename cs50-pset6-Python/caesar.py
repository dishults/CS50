#!/usr/local/bin/python3
# Program that encrypts messages using Caesar’s cipher
from sys import argv

def	main():
	nb = get_number()
	txt = get_text()
	encrypt(nb, txt)

def	get_number():
	try:
		number = int(argv[1])
		if(len(argv) == 2):
			return(number)
		else:
			exit('Usage: python caesar.py k')
	except:
		exit('Usage: python caesar.py k')

def	get_text():
	txt = input('plaintext: ')
	return (txt)

def	encrypt(nb, txt):
	for c in txt:
		if c.islower():
			print(chr((ord(c) + nb) % 97 % 26 + 97), end="")
		elif c.isupper():
			print(chr((ord(c) + nb) % 65 % 26 + 65), end="")
		else:
			print(c, end="")
	print()

if __name__ == "__main__":
	main()