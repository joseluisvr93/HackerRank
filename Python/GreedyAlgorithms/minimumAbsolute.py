#!bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    res = math.inf
    arr = sorted(arr)
    if len(set(arr)) == len(arr):
        for i in range(math.ceil(len(arr)/2)):
            d1 = abs(arr[i]-arr[i+1])
            d2 = abs(arr[-(i+1)]-arr[-(i+2)])
            d = min(d1,d2)
            if d == 1:
                res = 1
                break
            if d < res:
                res = d
    else:
        res = 0
    print(res)
    return res
    # Write your code here


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = minimumAbsoluteDifference(arr)

