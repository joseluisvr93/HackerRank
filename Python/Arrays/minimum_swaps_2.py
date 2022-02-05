import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    res = 0
    indexes = {value:key for key, value in enumerate(arr)}
    for i in range(len(arr)):
        if i != indexes[i+1]:
            temp = indexes[i+1]
            indexes[i+1]=i
            indexes[arr[i]] = temp
            arr[temp] = arr[i]
            arr[i] = i+1
            res +=1
            # print(a)
    return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    print(res)

