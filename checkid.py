def chh(a):
    if a % 2 == 0:
        return "even"
    elif a % 2 != 0:
        return "odd"
    else:
        return 0
    
d =int(input("enter number: "))
z = chh(d)    
print(z)