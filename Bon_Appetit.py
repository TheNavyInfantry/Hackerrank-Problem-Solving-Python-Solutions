#bill: an array of integers representing the cost of each item ordered
#k: an integer representing the zero-based index of the item Anna doesn't eat
#b: the amount of money that Anna contributed to the bill

def bonAppetit(bill, k, b):
    actualBill = (sum(bill) - bill[k]) // 2

    if b == actualBill:
        print('Bon Appetit')
    else:
        print(b - actualBill)


bonAppetit([3,10,2,9],1,12) #TEST CASE
