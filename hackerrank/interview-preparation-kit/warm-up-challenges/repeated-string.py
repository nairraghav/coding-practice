#!/bin/python3
"""
https://www.hackerrank.com/challenges/repeated-string/problem
"""

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    length_of_s = len(s)
    s_repeats = n // length_of_s
    remainder_of_s = n % length_of_s
    number_of_a_in_s = 0
    number_of_a_in_substring = 0
    for character in s:
        if character == "a":
            number_of_a_in_s += 1
    for character in s[:remainder_of_s]:
        if character == "a":
            number_of_a_in_substring += 1
    return (s_repeats * number_of_a_in_s) + number_of_a_in_substring

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
