def bonAppetit(bill, k, b):
    res = bill
    res[k] = 0
    op = (sum(res)/2) - b
    if op == 0:
        print("Bon Appetit")
    else:
        print(-int(op))
    return 0

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())
bonAppetit(bill, k, b)
