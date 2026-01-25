a = int(input("enter a: "))
c = input ("operation: ")
b = int(input("enter b: "))

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "power":
    print(a**b)
elif c == "%":
    print(a%b)
elif c == "/":
    print(a/b)
else:
    print("wronf input")


