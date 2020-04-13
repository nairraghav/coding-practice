#!/bin/python3
"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
"""


import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    num_of_rotations = d % len(a)
    b = a[num_of_rotations:]
    for num in a[0:num_of_rotations]:
        b.append(num)
    return b


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
