def countSwaps(a):
    # Write your code here
    res = 0
    for _ in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                res += 1
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    print("Array is sorted in "+str(res)+" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[-1]))
    return True

n = int(input().strip())

a = list(map(int, input().rstrip().split()))

countSwaps(a)
