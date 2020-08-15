def catAndMouse(catA, catB, mouseC):
    diff1 = abs(catA - mouseC)
    diff2 = abs(catB - mouseC)

    if diff1 < diff2:
        return 'Cat A'
    elif diff2 < diff1:
        return 'Cat B'
    elif diff1 == diff2:
        return 'Mouse C'


print(catAndMouse(1,2,3)) #test case1
print(catAndMouse(1,3,2)) #test case2