#https://www.hackerrank.com/challenges/time-conversion/problem

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    arr = s.split(':')
    hour = arr[0]
    minute = arr[1]
    seconds = arr[2][:-2]
    if 'PM' in arr[2] or 'pm' in arr[2]:
        if int(hour) != 12:
            hour = int(hour) + 12
    elif 'AM' in arr[2] or 'am' in arr[2]:
        if int(hour) == 12:
            hour = '00'

    return str(hour) + ':' + str(minute) + ':' + str(seconds)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()