#!/bin/pthon3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    moves = 0
    chaotic = 0
    for i, datum in enumerate(q):
        x = (i + 1) - datum
        chaotic += x
        if x < -2:
            return "Too chaotic"
        else:
            for j in range(max(0,datum-2),i):
                if datum < q[j]:
                    moves += 1
    return moves

    # Write your code here

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
