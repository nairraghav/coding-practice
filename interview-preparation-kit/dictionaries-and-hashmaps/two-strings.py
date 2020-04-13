#!/bin/python3
"""
https://www.hackerrank.com/challenges/two-strings/problem
"""


import math
import os
import random
import re
import sys


def twoStrings(s1, s2):
    first_string_set = set()
    for character in s1:
        first_string_set.add(character)
    
    for character in s2:
        if character in first_string_set:
            return "YES"
    
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
