from collections import Counter
from itertools import permutations

def sherlockAndAnagrams(s):
    res = 0
    for j in range(len(s)-1):
        text = []
        for k in range(len(s)-j):
            temp=[k]
            for m in range(k+1,j+k+1):
                temp.append(m)
            text.append([s[j] for j in temp])
        for k in range(len(text)):
            for i in range(k+1,len(text)):
                if Counter(text[i])==Counter(text[k]):
                    res+=1
    print(res)
    return res



q = int(input().strip())
for q_itr in range(q):
    s = input()
    result = sherlockAndAnagrams(s)
