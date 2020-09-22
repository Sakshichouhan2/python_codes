Email = input("Enter Your E-mail: ").strip() #Remove spaces at the beginning and at the end of the string

#Slice the User name
User_name = Email[:Email.index("@")]

#Slice the Domain name
Domain_name = Email[Email.index("@")+1:]

Result = "Your username is '{}'and your domain name is '{}'".format(User_name,Domain_name)

print(Result)

