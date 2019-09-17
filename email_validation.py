import re
email = input("enter an email ")

m = re.search('[^@]+@[^@]+\.[^@]+',email)

if m:
	print("Valid Email.")
else:
	print("Invalid Email.")
