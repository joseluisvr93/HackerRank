from collections import Counter

def isValid(s):
    x = Counter(s)
    y = Counter(x.values())
    print(x)
    print(y)
    if len(y)==1:
        print('YES')
        return 'YES'
    if len(y)==2:
        max_key = max(y.keys())
        min_key = min(y.keys())
        max_count = y[max_key]
        min_count = y[min_key]
        if min_key==1 & min_count==1:
            print('YES')
            return 'YES'
        if abs(max_key-min_key) == 1:
            if max_count==1:
                print('YES')
                return 'YES'
            if min_count==1:
                print('YES')
                return 'YES'
    print('NO')
    return 'NO'
    # aaaabbcc

s = input()

result = isValid(s)


