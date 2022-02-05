from collections import Counter
# Complete the freqQuery function below.
def freqQuery(queries): 
    struct1=Counter()
    struct2=Counter()
    result=[]
    for op,value in queries:
        if op==1:
            struct2[struct1[value]]-=1
            struct1[value]+=1
            struct2[struct1[value]]+=1
        elif op==2:
            if struct1[value]>0:
            struct2[struct1[value]]-=1
            struct1[value]-=1
            struct2[struct1[value]]+=1
        else:
            if struct2[value] > 0:
                result.append(1)
            else:
                result.append(0)


q = int(input().strip())
queries = []
for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))
ans = freqQuery(queries)

