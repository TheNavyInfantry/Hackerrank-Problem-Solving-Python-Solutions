def kangaroo(x1, v1, x2, v2):
    if (v1>v2) and (x1 - x2)%(v2 - v1) == 0:
        return 'YES'
    else:
        return 'NO'


print(kangaroo(0,3,4,2)) #Checks for 'YES'
print(kangaroo(0,2,5,3)) #Checks for 'NO'