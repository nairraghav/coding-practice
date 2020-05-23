"""
https://www.hackerrank.com/challenges/text-wrap/problem

You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

Output Format

Print the text wrapped paragraph.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""


#!/bin/python3

import textwrap

def wrap(string, max_width):
    new_string = ""
    count = 1
    for character in string:
        if count % max_width == 0:
            new_string = new_string + character + "\n"
        else: 
            new_string = new_string + character
        count += 1
    
    return new_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)