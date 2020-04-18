#!/bin/python3
"""
https://www.hackerrank.com/challenges/mark-and-toys/problem
"""


import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    # sort prices
    prices.sort()

    # for each price, check if we can afford and add it to the list
    amount_spent = 0
    toys_bought = 0
    for price in prices:
        if amount_spent + price < k:
            amount_spent += price
            toys_bought += 1
        else:
            break
    
    return toys_bought
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
