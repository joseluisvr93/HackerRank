def twoStrigs(s1, s2):
    for s in s1:
        if s in s2:
            return "YES"
    return "NO"
    # Write your code here

q = int(input().strip())
for q_itr in range(q):
    s1 = input()
    s2 = input()
    result = twoStrigs(s1, s2)
    print(result)

