# https://www.hackerrank.com/contests/hack-the-interview-u-s-2/challenges/high-security-strings
"""
Estimating the strength of any password is an important aspect of Information Security. In this challenge, your task is to calculate the strength of a given password in terms of weights assigned to the characters.

A password consists of English lowercase letters only.
Each English lowercase letter has assigned an integer weight in the range from 0 to 25 inclusive in such a way that the weight of letter  is given explicitly and weights of other letters follow in cyclic order. For example, if , then , , , , , , .
The strength of a password is the sum of weights of all characters the password consists of
Consider the following example. Let the password be  and the weight of letter  be 10. Then, the weights of all letters of the password are: , , , , , , , so the strength of the password is .

Input Format

In the first line, there is a string  denoting the password.

In the second line, there is an integer  denoting the weight of letter 

Constraints

 consists of English lowercase letters only
Output Format

The only line of the output must contain an integer denoting the strength of the password.

Sample Input 0

hellomrz
2
Sample Output 0

91
Explanation 0

The password is "hellomrz" and the weight of  is 2, so the weights of all letters of the password are: , , , , , , . The strength of the password is then .

Sample Input 1

aaaaa
1
Sample Output 1

5
Explanation 1

The password is "aaaaa" and the weight of  is 1, so the strength of the password is  as it consists of 5 letters .
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getStrength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING password
#  2. INTEGER weight_a
#

def getStrength(password, weight_a):
    # Complete the function

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    password = input()

    weight_a = int(input().strip())

    strength = getStrength(password, weight_a)

    fptr.write(str(strength) + '\n')

    fptr.close()
