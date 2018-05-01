# https://www.hackerrank.com/challenges/compare-the-triplets/problem

#!/bin/python3

import os
import sys

#
# Complete the solve function below.
#
def solve(a0, a1, a2, b0, b1, b2):
    A_score = 0
    B_score = 0

    a_score, b_score = get_score(a0, b0)
    A_score += a_score
    B_score += b_score

    a_score, b_score = get_score(a1, b1)
    A_score += a_score
    B_score += b_score

    a_score, b_score = get_score(a2, b2)
    A_score += a_score
    B_score += b_score

    return A_score, B_score


def get_score(a, b):
    a_score = 0
    b_score = 0
    if a > b:
        a_score = 1
    elif a < b:
        b_score = 1
    return a_score, b_score


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a0A1A2 = input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
