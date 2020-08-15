def hurdleRace(k, height):

    if k < max(height):
        return max(height)-k
    else:
        return 0

print(hurdleRace(4,[1,6,3,5,2])) #test case1
print(hurdleRace(5,[2,5,4,5,2,5])) #test case2