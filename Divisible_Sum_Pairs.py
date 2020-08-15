def divisibleSumPairs(n, k, arr):
    pair = 0
    for i in range(n):
        for j in range(n):
            if i < j and (arr[i]+arr[j]) % k == 0:
                pair += 1
    return pair

print(divisibleSumPairs(6,3,[1,2,3,4,5,6])) #test case