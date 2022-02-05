def birthday(s, d, m):
    # Write your code here
    res = 0
    for i in range(len(s)-m+1):
        suma = 0
        for j in range(m):
            suma += s[i+j]
        if suma == d:
            res += 1
    return res

n = int(input().strip())
s = list(map(int, input().rstrip().split()))
first_multiple_input = input().rstrip().split()
d = int(first_multiple_input[0])
m = int(first_multiple_input[1])
result = birthday(s, d, m)
print(result)
