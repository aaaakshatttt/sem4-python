age = int(input("enter age : "))
id = input("voter id? ")

if age > 18 and (id == "yes" or id ==  'Yes'):
    print("yyoure eligible")
elif age > 18 and (id == "no" or id == "No"):
    print("no id")
elif age < 18 and (id == "yes" or id ==  'Yes'):
    print("underage")
       