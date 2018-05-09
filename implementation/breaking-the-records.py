# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


#!/bin/python3

import os
import sys

#
# Complete the breakingRecords function below.
#
def breakingRecords(score):
    nb_best_score_increased = 0
    nb_worst_score_decreased = 0
    max_score = score[0]
    min_score = score[0]

    for i in range(1, len(score)):
        if score[i] > max_score:
            nb_best_score_increased += 1
            max_score = score[i]
        if score[i] < min_score:
            nb_worst_score_decreased += 1
            min_score = score[i]

    return [nb_best_score_increased, nb_worst_score_decreased]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
