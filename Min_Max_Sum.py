def miniMaxSum(arr):
    arrSorted = sorted(arr)
    print('{} {}'.format(sum(arrSorted[:len(arr)-1]),sum(arrSorted[1:])))


##EXTRA##

def miniMaxSum(arr):
    totalSum = sum(arr)
    minSum = totalSum - max(arr)
    maxSum = totalSum - min(arr)
    print(minSum,maxSum)
