def luckBalance(k, contests):
    x1 = [i for i,j in contests]
    x2 = [j for i,j in contests]
    res = 0
    mink = sum(x2) - k
    y = 0
    mask = [i==1 for i in x2]
    nx1 = [x1[i] for i in range(len(x1)) if mask[i]]
    print(mask)
    for i in sorted(nx1):
        if y < mink:
            res += i
            y += 1
        else:
            break

    res = sum(x1) - (res*2)
    print(res)
    return res
    # Write your code here

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
contests = []
for _ in range(n):
    contests.append(list(map(int, input().rstrip().split())))
result = luckBalance(k, contests)
