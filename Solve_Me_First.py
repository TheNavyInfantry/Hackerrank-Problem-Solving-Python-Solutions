def solveMeFirst(a,b):
	return a + b

num1 = int(input()) #getting inp1
num2 = int(input()) #getting inp2
res = solveMeFirst(num1,num2)
print(res)

##EXTRA##

def solveMeFirst(a,b):
	return a + b

num1,num2 = input('>> ').split() #getting inputs as an string then seperating
res = solveMeFirst(int(num1),int(num2))
print(res)