#Basic python code for Rock-Paper-scissors game
#Conditions:
#Rock beats Scissor
#Scissor beats Paper
#Paper beats Rock

Reshu = input("Enter Your Choice for Reshu: ")
Neha = input("Enter Your Choice for Neha: ")

def Compare(Reshu,Neha):
	if Reshu == Neha:
		return("Its a Tie")
	elif Reshu == "Rock":
		if Neha == "Scissor":
			return("Reshu Wins")
	elif Reshu == "Scissor":
		if Neha == "Paper":
			return("Reshu Wins")
	elif Reshu == "Paper":
		if Neha == "Rock":
			return("Neha Wins")
	elif Reshu == "Scissor":
		if Neha == "Rock":
			return("Neha Wins")
	elif Reshu == "Paper":
		if Neha == "Scissor":
			return("Neha Wins")
	elif Reshu == "Rock":
		if Neha == "Paper":
			return("Neha Wins")

	else:
		return("Invalid input! You have not entered rock, paper or scissors, try again")

print(Compare(Reshu,Neha))
print(Compare(Neha,Reshu))