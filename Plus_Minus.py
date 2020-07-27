def plusMinus(arr):
    pos = []
    neg = []
    zero = []

    for i in arr:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
        else:
            zero.append(i)


    print('{:.6f}'.format(len(pos) / len(arr)),'\n'
          '{:.6f}'.format(len(neg) / len(arr)),'\n'
          '{:.6f}'.format(len(zero)/len(arr)))

plusMinus([-4,3,-9,0,4,1])


