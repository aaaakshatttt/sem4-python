age = int(input("enter age: "))
marks =int(input("enter marks: "))
#we taking input from the user thats why we using inpuy() and when we use input we can print enter your name without useng print()
#but we entering age so its a number so in order to take number as an input we use int()

if age >= 18 and marks >= 40:
    print("eligible and passed")
elif age >=18 and marks < 40:
    print("eligible but failed")
else:
    print("not eligible")

