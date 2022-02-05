def maxMin(k, arr):
    arr.sort()
    min = arr[len(arr)-1]
    for i in range(len(arr)-k+1):
        res = arr[i+k-1] - arr[i]
        if res < min:
            min = res
    return min

n = int(input().strip())

k = int(input().strip())

arr = []

for _ in range(n):
    arr_item = int(input().strip())
    arr.append(arr_item)

result = maxMin(k, arr)
print(result)
