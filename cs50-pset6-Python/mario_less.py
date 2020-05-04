height = int(input('Height: '))
spaces = height - 1
while spaces + 1:
	hashes = height - spaces
	for i in range(spaces):
		print(" ", end="")
	for j in range(hashes):
		print("#", end="")
	spaces -= 1
	print()