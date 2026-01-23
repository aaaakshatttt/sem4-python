#declaring variables so each house have a box and later we will keep adding points
Gryffindor = 0
Ravenclaw  = 0
Hufflepuff = 0
Slytherin = 0
#printed first qiuestion
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
#declaring a variable 'a' to store the input answer as digit so using int()and we talking input from user so input()
a = int(input("enter your choice: "))
#ifelse statements
if a == 1: #if the choice is 1 so the variable gryffindor which originally had 0 points will now have 1
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
#after all the questions now we want to print all the points of all houses so in inverted commas print() prints whatever is written inside the commas but if i write print(griffindor) then the print() will print the value of the variable griffindor which we declared earlier but so do both
#to do both i did print("Slytherin",Slytherin) so in inverted commas it printed whatever its wrutten and after coma it will print value of variable
print("Slytherin",Slytherin)

print("Hufflepuff",Hufflepuff) 

print("Ravenclaw ",Ravenclaw) 

print("Gryffindor",Gryffindor) 

print("----------------------------------------")
# the program also asked for bonus note if i can printy the variable with the highest points soooo

if Slytherin > Hufflepuff  and Slytherin > Ravenclaw and Slytherin > Gryffindor:
  print("Slytherin",Slytherin)
elif Hufflepuff > Slytherin  and Hufflepuff > Ravenclaw and Hufflepuff > Gryffindor: 
  print("Hufflepuff",Hufflepuff) 
elif Ravenclaw > Hufflepuff  and Ravenclaw > Slytherin and Ravenclaw > Gryffindor:
  print("Ravenclaw ",Ravenclaw)
else:
  print("Gryffindor",Gryffindor)





