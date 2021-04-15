import random

#numList = (1, 5, 7, 13, 50, 120, 300, 320, 400, 700)
numList = (17, 77, 123, 173, 179, 192, 198, 204, 209, 239, 243, 313, 
            322, 337, 372, 394, 456, 462, 468, 495, 497, 499, 507, 537, 
            539, 558, 597, 605, 620, 624, 638, 653, 659, 671, 680, 685, 
            727, 739, 778, 788, 807, 810, 856, 880, 890, 903, 941, 991)
for k in range(10):
    cntSum = 0
    for i in range(10000):
        rndNum = numList[random.randint(0,9)]
        for n in numList:
            cntSum += 1
            if n == rndNum:
                break
    print(cntSum/10000)