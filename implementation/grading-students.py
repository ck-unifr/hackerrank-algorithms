# https://www.hackerrank.com/challenges/grading/problem


#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        if grade >= 38 and grade % 5 >= 3:
            grade = grade + (5 - grade % 5)
        new_grades.append(grade)

    return new_grades


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
