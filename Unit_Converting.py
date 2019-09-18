#Unit Converting

import math
import time
print ("130°c")

unit1 = input("which unit you want to convert from: ")
unit2 = input("which unit you want to convert to: ")
num = input("enter your value: ")

if unit1 == "cm" and unit2 == "m":
    ans = float(num)/100
    print (ans)
elif unit1 == "mm" and unit2 == "cm":
    ans = float(num)/10
    print (ans)
elif unit1 == "m" and unit2 == "cm":
    ans = float (num)*100
    print (ans)
elif unit1 == "cm" and unit2 =="mm":
    ans = float (num1)*10
    print (ans)
elif unit1 == "mm" and unit2 =="m":
    ans = float (num1)/1000
    print (ans)
elif unit1 == "m"and unit2 == "mm":
    ans = float (num1)/1000
    print (ans)
elif unit1 == "km" and unit2 == "m":
    ans = float (num1)/1000
    print (ans)
elif unit1 == "m" and unit2 == "km":
    ans = float (num1)/1000
    print (ans)
elif unit1 == "mm" and unit2 == "km":
    ans = float (num1)/1000000
    print (ans)
else:
    print ("Invalid choice")
