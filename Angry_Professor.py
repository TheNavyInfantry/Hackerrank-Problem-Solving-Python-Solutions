def angryProfessor(k, arr):

    arrivalOnTime = [each for each in arr if each <= 0]

    if len(arrivalOnTime) < k:
        return 'YES' #Class canceled
    elif len(arrivalOnTime) >= k:
        return 'NO' #Class did not canceled


print(angryProfessor(3,[-1,-3,4,2])) #test case1
print(angryProfessor(2,[0,-1,2,1])) #test case2