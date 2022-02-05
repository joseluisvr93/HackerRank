from collections import Counter

def makeAnagram(a, b):
    # Write your code here
    a1 = Counter(a)
    b1 = Counter(b)
    c = a1 - b1
    d = b1 - a1
    print(c)
    print(d)
    lenC = sum([i for i in c.values()])
    lenD = sum([i for i in d.values()])
    res = lenC + lenD
    print(str(res))
    return res

a = input()
b = input()
res = makeAnagram(a, b)
