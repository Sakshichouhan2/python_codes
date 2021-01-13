#Reverse String Script
#Step 1: Create a loop to read each character of the String one by one.
#Step 2: Declare an empty String.
#Step 3: Concatenate the read character at the beginning of the string.
def reverse(str):
	a = ''
	for i in str:
		a = i + a
	return a

# given string
mystr = input("Enter Your String: ")
print("Given String: ", mystr)

# reversed string
print("Reversed String: ", reverse(mystr))
