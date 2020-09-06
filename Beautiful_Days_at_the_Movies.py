def beautifulDays(i, j, k):
    count = 0
    for n in range(i,j+1):
        reversedNum = int(str(n)[::-1]) #Check line 15 for better understanding
        if (n - reversedNum) % k == 0:
            count += 1

    return count


print(beautifulDays(20,23,6)) #TEST CASE1
print(beautifulDays(13,45,3)) #TEST CASE2


# #Number reversing method using string slicing
# userInp = int(input('Your number: '))
# userInp = int(str(userInp)[::-1])
# print(userInp)
