def utopianTree(n):
    startingHeight = 1 #default starting height of planted tree
    for i in range(1,n+1):
        if i % 2 != 0:
            startingHeight *= 2
        else:
            startingHeight += 1

    return startingHeight

#odd result is spring, means *2 ; even result is summer, means +1