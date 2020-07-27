def compareTriplets(a,b):
    user1 = 0
    user2 = 0

    for i,j in zip(a,b):
        if i > j:
            user1 += 1
        elif j > i:
            user2 += 1

    return f'{user1} {user2}'

print(compareTriplets([17,28,30],[99,16,8]))