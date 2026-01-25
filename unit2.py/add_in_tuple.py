tuplex = (1,2,3,4,5,6,7,8)
listx = list(tuplex) #type conversion tuple to list
#now tuple is conveerted to list and the list is stored in a variable names 'listx'
listx.append(9)#as we know elements cannt be added in tuple but can be added in list
listx.append(10)
tuplex = tuple(listx)
print(tuplex)