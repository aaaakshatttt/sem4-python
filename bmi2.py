def bmi(a,b):
    return a/b**2

mass = int(input("enter mass: "))
height = int(input("enter height: "))
bodymassindex = bmi(mass,height)
print(bodymassindex)