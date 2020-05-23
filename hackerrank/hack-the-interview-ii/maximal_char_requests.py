"""
Product Distribution

A company has requested to streamline their product allocation strategy, and given  products, each of which has an associated value, you are required to arrange these products into segments for processing. There are infinite segments indexed as 1, 2, 3 and so on.

However, there are two constraints:

You can assign a product to a segment with index  if and only if  or the segment with index  has at least  products.
Any segment must contain either no products or at least  products.
The score for a segment is defined as the index of the segment multiplied by the sum of values of the products it contains. The score of an arrangement of products is the sum of scores of segments. Your task is to compute the maximum score of an arrangement.

Consider, for example,  products and . One optimal way to assign is -

Assign the first three products to segment 1.
Assign the next three products to segment 2.
Assign the next five products to segment 3.
Note that we can not assign 2 products to segment 4 as the second constraint would be violated. The score of the above arrangement is -

1 * (1 + 2 + 3) + 2 * (4 + 5 + 6) + 3 * (7 + 8 + 9 + 10 + 11) = 6 + 30 + 135 = 171.

Since the arrangement score can be very large, print it modulo .

Input Format

In the first line, there are two space-separated integers  and .

In the second line, there are  space-separated integers  denoting the values associated with the products.

Constraints

Output Format

In a single line, print a single integer denoting the maximum score of the arrangement modulo .

Sample Input 0

5 2
1 5 4 2 3
Sample Output 0

27
Explanation 0

The array is  and . It is optimal to put the first and fourth products into the first segment and the remaining products to the second segment. Doing that, we get the arrangement score  which is the greatest score that can be obtained. Finally, the answer is  modulo  which is .

Sample Input 1

4 4
4 1 9 7 
Sample Output 1

21
Explanation 1

All the four products must be placed in the first segment. The score in this case will be 1 * (4 + 1 + 9 + 7) = 21.
"""



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxCharCount' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. 2D_INTEGER_ARRAY queries
#

def get_max_char_count(s, x, y):
    current_char = s[x].lower()
    char_count = {current_char:1}
    for index in range(x+1, y+1):
        new_char = s[index].lower()
        if current_char < new_char:
            current_char = new_char
        if new_char in char_count:
            char_count[new_char] += 1
        else:
            char_count[new_char] = 1
    return char_count[current_char]
        
    

def getMaxCharCount(s, queries):
    answers = []
    for query in queries:
        x,y = query
        answers.append(get_max_char_count(s, x, y))
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    q = int(input().strip())

    query = []

    for _ in range(q):
        query.append(list(map(int, input().rstrip().split())))

    ans = getMaxCharCount(s, query)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
