#!/bin/python3
"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
"""

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    current_index = 0
    last_index = len(c) - 1
    hops = 0
    while current_index != last_index:
        if (current_index + 2 <= last_index) and (c[current_index + 2] == 0):
            current_index += 2
        else:
            current_index += 1
        hops += 1
    return hops

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
