# https://www.hackerrank.com/contests/hack-the-interview-u-s-2/challenges/heads-or-tails
"""
Maximum Streaks

A coin was tossed numerous times. You need to find the longest streak of tosses resulting  and the longest streak of tosses resulting in .

Formally, given the results of  tosses of a coin, find the maximum number of consecutive  and the maximum number of consecutive .

Consider the following example: a coin was tossed  times and the results were . Therefore, the longest  streak was  and the longest  streak was .

Complete the function getMaxStreaks which takes an array of strings toss and returns an array of two integers denoting the maximum streaks of  and  respectively.

Input Format

In the first line, there is a single integer  denoting the number of tosses.

Then,  lines follow. The  of them contains a string  denoting the result of the  toss of the coin.

Constraints

Output Format

In a single line, print two space-separated integers denoting the maximum streak of  and the maximum streak of  respectively.

Sample Input 0

7
Heads
Tails
Tails
Tails
Heads
Heads
Tails
Sample Output 0

2 3
Explanation 0

The longest streak of  is 2 and the longest streak of  is 3.

Sample Input 1

3
Tails
Tails
Tails
Sample Output 1

0 3
Explanation 1

The longest streak of  is 0 since there were no such tosses, and the longest streak of  is 3.

Sample Input 2

4
Heads
Heads
Heads
Heads
Sample Output 2

4 0
Explanation 2

The longest streak of  is 4, and the longest streak of  is 0 since there were no such tosses.
"""



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxStreaks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY toss as parameter.
#

def getMaxStreaks(tosses):
    max_heads_streak = 0
    max_tails_streak = 0
    current_heads_streak = 0
    current_tails_streak = 0
    for toss in tosses:
        if toss == "Heads":
            max_tails_streak = max(max_tails_streak, current_tails_streak)
            current_tails_streak = 0
            current_heads_streak += 1
        else:
            max_heads_streak = max(max_heads_streak, current_heads_streak)
            current_heads_streak = 0
            current_tails_streak += 1
    max_tails_streak = max(max_tails_streak, current_tails_streak)
    max_heads_streak = max(max_heads_streak, current_heads_streak)
    return (max_heads_streak, max_tails_streak)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    toss_count = int(input().strip())

    toss = []

    for _ in range(toss_count):
        toss_item = input()
        toss.append(toss_item)

    ans = getMaxStreaks(toss)

    fptr.write(' '.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
