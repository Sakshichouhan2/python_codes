f=open('Phone.txt','w+')
def Phone_book():
    print('1. Show Contact')
    print('2. Add Contact')
    print('3. Remove Contact')
    print('4. Existing Contact')
numbers = {}
menu_choice = 0
Phone_book()
while Phone_book != 4:
    Phone_book = int(input("Choice a number: "))
    if Phone_book == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = int(input("Number: "))
        f.write(name)
        numbers[name] = phone
    elif Phone_book == 3:
        print("Remove Name and Number")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    elif Phone_book == 1:
        print("Lookup Number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif menu_choice != 4:
        menu()

f.close()