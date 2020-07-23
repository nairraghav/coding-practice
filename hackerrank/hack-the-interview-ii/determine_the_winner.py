# https://www.hackerrank.com/contests/hack-the-interview-u-s-2/challenges/playing-cards-1-1
"""
Determine the Winner

A deck of cards contains 52 cards, where each card has a suit and a number written on it. There are 4 suits, namely  and , and numbers on cards are from range  to .

Before the game starts, one of the suits is decided to be called the winning suit. Then, the play begins and two players play exactly  rounds as follows:

first, each player draws a single card from the deck
if one of the players drew a card of the winning suit and the other did not, then the player who drew a card of the winning suit wins the round
otherwise, the numbers written on the cards decide: if one player drew a card with a greater number on it than the other player, the player with the greater number wins, otherwise, if both players drew cards with the same numbers, the round ends in a draw
after the round is ended, the players return the cards they drew into the deck
Given the cards the players drew in each round, determine the result of each round of the game.

Input Format

In the first line, there is a single character  denoting the winning suit.

In the second line, there is a single integer  denoting the number of rounds to be played.

Each of the next  lines denotes the cards that were drawn in a single round of the game and contains four space-separated values: , and  denoting the suit of player's 1 card, the number on player's 1 card, the suit of player's 2 card, and the number of player's 2 card respectively.

Constraints

Output Format

The output must contain exactly  lines. The  of those lines must denote the result of the  round of the game and contain either Player 1 wins if Player 1 wins or Player 2 wins if Player 2 wins, or Draw if the round ends in a draw.

Sample Input 0

B
5
A 2 B 1
A 7 D 2
B 5 D 13
B 3 B 1
A 12 C 12
Sample Output 0

Player 2 wins
Player 1 wins
Player 1 wins
Player 1 wins
Draw
Explanation 0

The winning suit is  and there are 5 rounds of the game.

In the first round, Player 2 drew a winning suit card and Player 1 did not, therefore, Player 2 wins.

In the second round, none of the players drew a winning suit card, so the numbers on the cards decide. Since Player 1 drew a card with a greater number than Player 2, Player 1 wins.

In the third round, Player 1 drew a winning suit card and Player 2 did not, therefore, Player 1 wins.

In the fourth round, both players drew a winning suit cards, so the numbers on the cards decide. Since Player 1 drew a card with a greater number than Player 2, Player 1 wins.

In the fifth round, none of the players drew a winning suit card, so the numbers on the cards decide. Since both players drew cards with the same numbers, the round results in a Draw.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getRoundResult' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. CHARACTER winning_suit
#  2. CHARACTER suit1
#  3. INTEGER number1
#  4. CHARACTER suit2
#  5. INTEGER number2
#

def getRoundResult(winning_suit, suit1, number1, suit2, number2):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    winning_suit = input()[0]

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        suit1 = first_multiple_input[0][0]

        number1 = int(first_multiple_input[1])

        suit2 = first_multiple_input[2][0]

        number2 = int(first_multiple_input[3])

        result = getRoundResult(winning_suit, suit1, number1, suit2, number2)

        fptr.write(result + '\n')

    fptr.close()
