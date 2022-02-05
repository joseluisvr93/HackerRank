def commonChild(s1, s2):
    """
    Given two strings, find the length of the longest common substring.
    """
    maxAt = {}

    for i1 in range(len(s1)):
        m = 0
        for i2 in range(len(s2)):
            potentialSum = m + 1
            temp = maxAt.get(i2, 0)
            if temp > m:
                m = temp
            if s1[i1] == s2[i2]:
                maxAt[i2] = potentialSum
    return max(maxAt.values(), default=0)

s1 = input()
s2 = input()
result = commonChild(s1, s2)
print(result)


