def maximumToys(prices, k):
    sPrices = sorted(prices)
    s = 0
    res = 0
    for p in sPrices:
        s += p
        if s < k:
            res += 1
        else:
            break
    print(res)
    return res
    # Write your code here

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
prices = list(map(int, input().rstrip().split()))
result = maximumToys(prices, k)
