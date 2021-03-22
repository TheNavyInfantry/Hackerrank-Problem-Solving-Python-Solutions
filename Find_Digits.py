def findDigits(n):
    count = 0

    for i in str(n):
        try:
            if n % int(i) == 0:
                count += 1

        except ZeroDivisionError:
            pass

        else:
            count = count

    return count


print(findDigits(124))  # Return 3
print(findDigits(111))  # Return 3
print(findDigits(10))  # Return 1
