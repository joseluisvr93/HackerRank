#!/bin/python3

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    result = []
    k = 0
    for i in range(0,len(arr)-2):
        for j in range(0,len(arr[0])-2):
            x = arr[0+i][0+j]+arr[0+i][1+j]+arr[0+i][2+j]
            x += arr[1+i][1+j]
            x += arr[2+i][0+j]+arr[2+i][1+j]+arr[2+i][2+j]
            result.append(x)
            k+=1
    return max(result)

if __name__ == '__main__':
    arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]

    result = hourglassSum(arr)

    print(result)
