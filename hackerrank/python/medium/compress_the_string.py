"""
https://www.hackerrank.com/challenges/compress-the-string/problem

In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string .

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of  denote integers between  and .


Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
Explanation

First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.

Also, note the single space within each compression and between the compressions.
"""


#!/bin/python3

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    string = input()
    compressed_string = []
    
    index = 1
    current_character = string[0]
    current_count = 1
    while index < len(string):
        if string[index] == current_character:
            current_count += 1
        else:
            compressed_string.append((current_count, int(current_character)))
            current_character = string[index]
            current_count = 1
        index += 1
    compressed_string.append((current_count, int(current_character)))
    final_string = ""
    for count_char in compressed_string:
        final_string += str(count_char) + " "
    final_string.strip()
    print(final_string)
