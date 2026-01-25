def check(a):
    if a%2==0:
        return "even"
    else:
        return "odd"

num = int(input("enter number:"))
com = check(num)
print(com)    