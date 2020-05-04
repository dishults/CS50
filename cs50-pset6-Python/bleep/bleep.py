#!/usr/bin/env python3
# Censores the words
from sys import argv


def main():
	words = get_banned_words().strip('\n').split()
	message = get_message().split()
	print_censored_msg(words, message)


def	get_banned_words():
	try:
		if(len(argv) == 2):
			with open(argv[1]) as f:
				words = f.read()
			f.closed
			return (words)
		else:
			exit('Usage: python bleep.py dictionary')
	except:
		exit('Usage: python bleep.py dictionary')

def	get_message():
	message = input('What message would you like to censor?\n')
	return (message)

def	print_censored_msg(words, message):
	for m in message:
		if m.lower() in words:
			for i in range(len(m)):
				print('*', end="")
		else:
			print(m, end="")
		if message.index(m) < len(message) - 1:
			print(' ', end="")
	print()


if __name__ == "__main__":
    main()
