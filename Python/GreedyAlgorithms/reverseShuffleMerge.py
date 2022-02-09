from itertools import permutations
# No complete solution
def reverseShuffleMerge(s):
    n = len(s)
    n2 = n//2
    s1 = s[:n2]
    s2 = s[n2:]
    reversedS1 = reverse(s1)
    shuffledS2 = shuffle(s2)
    if reversedS1 < shuffledS2:
        return reversedS1
    else:
        return shuffledS2

def reverse(s):
    return s[::-1]

def shuffle(s):
    perms = [''.join(p) for p in permutations(s)]
    perms = list(set(perms))
    min = ""
    for i in range(len(perms)):
        if i == 0:
            min = perms[i]
        if perms[i] < min:
            min = perms[i]

    return min

def merge(s,t):
    return s+t
    

s = input()
result = reverseShuffleMerge(s)
print(result)

