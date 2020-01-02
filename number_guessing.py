#Python Script for Number Guessing 
import random
try:
	hidden_number = random.randrange(1,1001)
	print(hidden_number)

	guess = int(input("Please enter your guess: "))
	if guess == hidden_number:
		print('You Guess Right Number')
	elif guess < hidden_number:
		print('Your Guess is too low')
	else:
		print('Your Guess is too high')
except ValueError:
	print("Enter a Valid Integer ")