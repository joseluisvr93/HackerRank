def formingMagicSquare(s):
    for i in range(len(s)):
        print(sum(s[i]))
    s2 = [s[i][j] for i in range(len(s)) for j in range(len(s[i]))]
    s2 = sorted(s2)
    res = 0
    for i in range(len(s2)):
        if (s2[i]) != (i+1):
            res += abs((s2[i]) - (i+1))
    return res
    # Write your code here

s = []
for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))
result = formingMagicSquare(s)
print(result)
