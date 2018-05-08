# https://www.hackerrank.com/challenges/kangaroo/problem

#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # jumps = 0
    # while True:
    #     dist1 = x1 + v1*jumps
    #     dist2 = x2 + v2*jumps
    #     jumps += 1
    #     if dist1 == dist2:
    #         return 'YES'
    #     elif x1 > x2 and dist2 > dist1:
    #         return 'NO'
    #     elif x2 > x1 and dist1 > dist2:
    #         return 'NO'

    if ((x1 < x2) and (v1 < v2)):
        return 'NO'
    elif ((v1 != v2) and ((x2 - x1) % (v1 - v2)) == 0):
        return 'YES'
    else:
        return 'NO'


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)