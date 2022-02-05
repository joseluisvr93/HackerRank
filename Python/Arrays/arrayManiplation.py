from itertools import accumulate
from collections import defaultdict
#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

queries = []

ar = defaultdict(int)
for _ in range(m):
    # queries.append(list(map(int, input().rstrip().split())))
    p, q, k = map(int, input().split())
    ar[p] += k
    ar[q + 1] -= k
    print(ar)
print(sorted(ar))
result = max(accumulate(ar[i] for i in sorted(ar)))
print(result)
# result = arrayManipulation(n, queries)

