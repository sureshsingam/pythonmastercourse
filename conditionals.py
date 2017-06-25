#Testing conditions  and function

def conditionalTest(num,rangeNum):
    if num < (rangeNum/2):
        print("{} is less than average number".format(num))
    elif num == (rangeNum/2):
        print("You are now half way to the list {} ".format(num))
    else:
        print("You are {}, it is past the mid point and have {} numbers left".format(num,rangeNum-num))

print("updating the conditional with looping")
rangeVal = range(1,11)
for i in rangeVal:
    conditionalTest(i,len(rangeVal))
