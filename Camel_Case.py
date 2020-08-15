def camelcase(s):
    count = 0
    is_upper = [n for n in s if n.isupper()]
    count += len(is_upper)+1  #+1 is for count the first word as a new line
    return count

print(camelcase('saveChangesInTheEditor')) # test case1
print(camelcase('isThisAnAcceptableCamelCaseOrNot')) # test case2