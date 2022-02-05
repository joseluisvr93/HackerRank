def alternatingCharacters(s):
    # Write your code here
    x = 0
    res = 0
    if s[0] == 'A':
        n = 'B'
    else:
        n = 'A'

    for letter in s:
        if x>0:
            if n==letter:
                if n == 'A':
                    n = 'B'
                else:
                    n = 'A'
            else:
                res +=1
        x += 1

    print(res)
    return res

q = int(input().strip())
for q_itr in range(q):
    s = input()
    result = alternatingCharacters(s)
