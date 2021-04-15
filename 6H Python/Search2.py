# 이진탐색 결과
import random

# numList = (1, 5, 7, 13, 50, 120, 300, 320, 400, 700)
numList = (17, 77, 123, 173, 179, 192, 198, 204, 209, 239, 243, 313, 
           322, 337, 372, 394, 456, 462, 468, 495, 497, 499, 507, 537, 
           539, 558, 597, 605, 620, 624, 638, 653, 659, 671, 680, 685, 
           727, 739, 778, 788, 807, 810, 856, 880, 890, 903, 941, 991)

for k in range(10):
    cntSum = 0
    for i in range(10000):
        start = 0
        end = len(numList) - 1
        key = int((start + end) / 2)
        V = random.randint(start, end)
        while True :
            cntSum += 1
            if numList[key] == numList[V] or start == end:
                break
            elif numList[key] < numList[V]:
                start = key + 1
                key = int((start + end) / 2)
            else:
                end = key - 1
                key = int((start + end) / 2)
    print(cntSum / 10000)