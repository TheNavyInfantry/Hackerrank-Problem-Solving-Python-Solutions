    # 4B - 1#
   ## 3B - 2#
  ### 2B - 3#
 #### 1B - 4#
##### 0B - 5#

def staircase(n):
    for i in range(1,n + 1): #NOTE1
        emp = ' '*(n - i)#NOTE2
        print(emp+i*'#')

staircase(5)

#NOTE1: If you dont start range from 1, it will assume starting point as 0 and
    # for this reason it will create an empty line at top of the staircase

#NOTE2: Let's say your n value is 5 and for loop will be starting from 1.
    # Template of loop will be like this ' '*(n-i)  [ex. '  '*(5-1)] and
    # while left side (n) were decreasing one by one, right side (i) will be increasing one by one