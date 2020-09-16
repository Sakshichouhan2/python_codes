def bank_trns():
	Customer_Name = input("Customer name as per the bank records: ")
	if (r'^[aA-zZ\s]+$', Customer_Name):
		print()
	else:
		print("Its an Invalid name",Customer_Name) 
	Account_Number = int(input("Enter Account Number: "))
	
	Re_enter_Account_Number = int(input("Re-Enter Account Number: "))
	if Account_Number == Re_enter_Account_Number:
		print(" ")
	else:
		print("Please Enter Correct Account Number")
	Bank_IFSC_Code = input("Enter IFSC Code: ")
	if ("^[A-Z]{4}0[A-Z0-9]{6}$",Bank_IFSC_Code):
		print("its a valid IFSC ",Bank_IFSC_Code)
	else:
		print("its an  invalid IFSC ",Bank_IFSC_Code)

	Bank_Name = input("Enter Bank Name: ")
	Branch_Name = input("Enter Branch Name: ")
	Account_Type = input("Saving & Current: ")

bank_trns()