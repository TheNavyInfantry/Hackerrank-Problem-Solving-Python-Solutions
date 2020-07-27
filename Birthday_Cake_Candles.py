def birthdayCakeCandles(ar):
    tallestCandle = 0
    for candle in ar:
        if candle is max(ar):
            tallestCandle += 1
    return tallestCandle
#!! Working but slow

##EXTRA##
def birthdayCakeCandles(ar):
    return ar.count(max(ar)) #Finding maxes in ar then counting how many there is
