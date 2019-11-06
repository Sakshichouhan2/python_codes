import re

Password = input("Enter Any Password to check it's a Valid Password ot Invalid Password: ")

x = 0
while True:
	if (len(Password)<8):
		x = -1
	elif not re.search("[a-z]", Password):
		x = -1
	elif not re.search("[A-Z]", Password):
		x = -1
	elif not re.search("[0-9]", Password):
		x = -1
	elif not re.search("[_@$]", Password):
		x = -1
	elif not re.search("\s" , Password):
		x = -1
	else:
		x = 0
		print("Valid Password")
if x == -1:
	print("Invalid Password")