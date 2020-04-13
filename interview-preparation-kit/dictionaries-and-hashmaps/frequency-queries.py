#!/bin/python3
"""
https://www.hackerrank.com/challenges/frequency-queries/problem
"""


import math
import os
import random
import re
import sys


def handle_operation(operation, value, frequencies):
    output = None
    if operation == 1:
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1
    elif operation == 2:
        if value in frequencies:
            if frequencies[value] > 1:
                frequencies[value] -= 1
            else:
                del frequencies[value]
    else:
        values = set(frequencies.values())
        if value in values:
            return frequencies, 1
        else:
            return frequencies, 0
    return frequencies, None
    
def freqQuery(queries):
    frequencies = {}
    outputs = []
    for query in queries:
        operation, value = query
        frequencies, output = handle_operation(operation, value, frequencies)
        if output != None:
            outputs.append(output)
    return outputs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
