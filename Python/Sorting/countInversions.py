def countInversions(arr):
    n = len(arr)
    if n==1:
        return 0
    else:
        n1 = n//2
        n2 = n - n1

        a1 = arr[:n1]
        a2 = arr[n1:]

        a = countInversions(a1)+countInversions(a2)

        i1, i2 = 0,0
        for i in range(n):
            if i1<n1 and (i2>=n2 or a1[i1]<=a2[i2]):
                arr[i]=a1[i1]
                a+=i2
                i1+=1
            elif i2 < n2:
                arr[i] = a2[i2]
                i2+=1
        return a


t=int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countInversions(arr)
    print(result)
