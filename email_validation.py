import re

Email = input("Enter Email to check it's a Valid Email ot Invalid Email: ")
x = 0
while Email:
	if not re.search("[a-z]", Email):
		x = -1
	elif not re.search("[0-9]", Email):
		x = -1
	elif not re.search("[_@.]", Email):
		x = -1
	else:
		x = 0
		print("Valid Email")
if x == -1:
	print("Invalid Email")
