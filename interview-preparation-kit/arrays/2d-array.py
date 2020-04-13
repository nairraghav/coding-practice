#!/bin/python3
"""
https://www.hackerrank.com/challenges/2d-array/problem
"""


import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglasses = []
    for i in range(4):
        for j in range(4):
            top_row = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom_row = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hourglasses.append(top_row + middle + bottom_row)
    return max(hourglasses)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
