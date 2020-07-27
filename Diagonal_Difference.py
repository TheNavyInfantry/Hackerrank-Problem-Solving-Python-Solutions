def diagonalDifference(arr):

    counter1 = 0
    counter2 = len(arr) - 1

    left_arr = []
    right_arr = []

    for i in range(len(arr)):
        left_arr.append(arr[counter1][counter1])
        counter1 +=1

    counter1 = 0
    for i in range(len(arr)):
        right_arr.append(arr[counter1][counter2])
        counter1 += 1
        counter2 -= 1

    return abs(sum(left_arr)-sum(right_arr))


arr = [[11, 2, 4],
       [4 , 5, 6],
       [10, 8, -12]]

print(diagonalDifference(arr))
