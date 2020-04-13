#!/bin/python3
"""
https://www.hackerrank.com/challenges/sock-merchant/problem
"""

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks_count = {}
    for sock in ar:
        if sock in socks_count:
            socks_count[sock] += 1
        else:
            socks_count[sock] = 1
    
    sock_pairs = 0
    for _,num_socks in socks_count.items():
        sock_pairs += num_socks // 2
    return sock_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
