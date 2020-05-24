def bank():
	Choice = input("Press 1. Create Account\n Press 2. Debite Balance\n Press 3. Credit Balance\n Press 4. Balance Inquery\n Press 5. Loan\n")
	if Choice == "1":
		print("Fill The Details")
		First_Name = input("Enter First Name: ")
		Last_Name  = input("Enter Last Name: ")
		Account_Type = input("Saving,Current\n")

	elif Choice == "2":
		Account_Holder = input("Enter Holder Name: ")
		Account_Number = int(input("Enter Account Number: "))
		Amount = int(input("Enter Amount in Words: "))
		Amount_Words = input("Enter Amount in Words: ")

	elif Choice == "3":
		Account_Holder = input("Enter Holder Name: ")
		Account_Number = int(input("Enter Account Number: "))
		Amount = int(input("Enter Amount in Words: "))
		Amount_Words = input("Enter Amount in Words: ")

	elif Choice == "4":

bank()