#https://www.hackerrank.com/challenges/staircase/problem

#!/bin/python3

import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    for i in range(n):
        str = ' '*(n-i-1) + '#'*(i+1)
        print(str)

if __name__ == '__main__':
    n = int(input())

    staircase(n)