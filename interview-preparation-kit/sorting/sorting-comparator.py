"""
https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem
"""

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return "{} has a score of {}".format(self.name, self.score)

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif b.score > a.score:
            return 11
        else:
            a_name_length = len(a.name)
            b_name_length = len(b.name)
            name_length = min(a_name_length, b_name_length)

            for index in range(name_length):
                if a.name[index] > b.name[index]:
                    return 1
                elif b.name[index] > a.name[index]:
                    return -1
                else:
                    pass
            if a_name_length == b_name_length:
                return 0
            elif a_name_length < b_name_length:
                return -1
            else:
                return 1
            


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)