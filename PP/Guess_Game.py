import random

c_guess = random.randint(1, 1000)
# print("Computer guess is:", c_guess)
i = 10
while i > 0:
	man = int(input("Enter a number: "))
	if man == c_guess:
		print("You win \nYour score is: ", i)
		exit(1)
	elif man < c_guess:
		print("Your number is lesser than computer guess")
	else:
		print("Your number is greater than computer guess")
	i -= 1

print("You loss\nYour score is: 0")
print("Computer guess is:", c_guess)
