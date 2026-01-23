Gryffindor = 0
Ravenclaw  = 0
Hufflepuff = 0
Slytherin = 0
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
a = int(input("enter your choice: "))
if a == 1:
  Gryffindor = Gryffindor + 1
  Ravenclaw  = Ravenclaw + 1
elif a == 2:
  Hufflepuff = Hufflepuff + 1
  Slytherin = Slytherin + 1
else:
  print("wrong inpupt")

print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
b = int(input("enter your choice: "))
if b == 1:
  Hufflepuff = Hufflepuff + 2
elif b == 2:
  Slytherin  = Slytherin + 2
elif b == 3:
  Ravenclaw = Ravenclaw + 2
elif b == 4:
  Gryffindor = Gryffindor + 2
else:
  print("wrong input")

print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

c = int(input("enter your chocice"))
if c == 1:
  Slytherin = Slytherin + 4
elif c == 2:
  Hufflepuff = Hufflepuff + 4
elif c == 3:
  Ravenclaw = Ravenclaw  + 4
elif c == 4:
  Gryffindor = Gryffindor + 4
else:
  print("wrong input")

print("Slytherin",Slytherin)

print("Hufflepuff",Hufflepuff) 

print("Ravenclaw ",Ravenclaw) 

print("Gryffindor",Gryffindor) 







