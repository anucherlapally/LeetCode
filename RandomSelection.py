import random
list1 = [1720,1342,1486,1684,1863,461,338,1356,136,762,476,868,1763,1009,693,268,191,401,67,190,405,645]
def randomselection(list1):
    list2 = []
    while len(list2) < 10:
        x =  random.choice(list1)
        if x not in list2:
            list2.append(x)

    print(list2)

randomselection(list1)