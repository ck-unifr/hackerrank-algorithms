# https://www.hackerrank.com/challenges/the-birthday-bar/problem

# Lily has a chocolate bar that she wants to share it with Ron for his birthday.
# Each of the squares has an integer on it.
# She decides to share a contiguous segment of the bar selected such that the length of the segment
# mathches Ron's birth month and the sum of the integers on the squares is equal to his birth day.
# You must determine how many ways she can divide the chocolate.


#!/bin/python3

import sys

def solve(n, s, d, m):
    # the length of the segment mathches Ron's birth month
    # the sum of the integers on the squares is equal to his birth day
    nb_solutions = 0
    for i in range(len(s)-m+1):
        nb_solutions += int(sum(s[i:i+m]) == d)
    return nb_solutions



n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
