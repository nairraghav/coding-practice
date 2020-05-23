#!/bin/python3
"""
https://www.hackerrank.com/challenges/counting-valleys/problem
"""

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    current_level = 0
    in_valley = False
    for step in s:
        if step == "U":
            current_level += 1
        else:
            current_level -= 1
        now_in_valley = current_level < 0
        if (in_valley) and (not now_in_valley):
            valleys += 1
        in_valley = now_in_valley
    return valleys
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
