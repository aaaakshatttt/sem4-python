def usd(a):
    if a == rupee:
        return a * 90
    elif a == yen:
        return a * 76
    else:
        return a * 44
    



yen = int(input("enter yen: "))
real = int(input("enter brazilian real: "))
rupee = int(input("enter rupeeeee: "))

riu = usd(rupee)
yid = usd(yen)
reiu = usd(real)
print (yid)
print(riu)
print(reiu)