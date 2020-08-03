# s=start point of house
# t=end point of house
# a=apple tree | m apple
# b=orange | n orange
# d=fall distance of fruit from tree| -d means; fell of left side | +d means; fell on right side

def countApplesAndOranges(s, t, a, b, apples, oranges):
    homeZoneApple = 0
    homeZoneOrange = 0
    for i in apples:
        if (a+(i)) >= s and (a+(i)) <= t:
            homeZoneApple += 1
    for j in oranges:
        if (b + (j)) >= s and (b + (j)) <= t:
            homeZoneOrange += 1

    print(homeZoneApple)
    print(homeZoneOrange)

countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4])

