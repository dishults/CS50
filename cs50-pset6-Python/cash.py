# Program that calculates the minimum number of coins required to give a change.
def	main():
	number = get_number()
	total = count_coins(number)
	print(total)

def	get_number():
	while True:
		number = input("Change owed: ")
		try:
			number = float(number)
			if number > 0:
				return number
		except:
			continue

def	count_coins(number):
	number = int(number * 100)
	quarters = int(number / 25)
	number %= 25
	dimes = int(number / 10)
	number %= 10
	nickels = int(number / 5)
	number %= 5
	pennies = int(number / 1)
	return quarters + dimes + nickels + pennies

if __name__ == "__main__":
	main()