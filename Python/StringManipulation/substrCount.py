def substrCount(n, s):
    res = n
    i = 0
    while i < n:
        repeat = 0
        while (i+1<len(s) and s[i]==s[i+1]):
            repeat += 1
            i += 1
        res += (repeat*(repeat+1))//2
        pointer = 1
        flag = 0
        while ((i+pointer<len(s)) and (i-pointer>=0) and (s[i+pointer]==s[i-pointer]) and (flag==0)):
            if pointer > 1 :
                if s[i+pointer-1] == s[i-pointer]:
                    res += 1
                    pointer += 1
                else:
                    flag = 1
            else:
                res += 1
                pointer += 1
        i += 1
    return res

n = int(input())
s = input()
result = substrCount(n, s)
print(result)
