def check(a):
    if a % 2 == 0:
        return "even"
    else:
        return "odd"

number = int(input("enter number:"))
huh = check(number)

print(huh)