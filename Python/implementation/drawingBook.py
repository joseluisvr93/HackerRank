import math

def pageCount(n, p):
    p2 = n - p
    h = p / 2
    h2 = (p2 / 2) 
    res1 = int(h)
    if n % 2 == 1:
        res2 = int(h2)
    else:
        res2 = int(math.ceil(h2))
    if res1 < res2:
        return res1
    else:
        return res2

n = int(input().strip())
p = int(input().strip())

result = pageCount(n, p)
print(result)
