def breakingRecords(scores):
    best_reccord_count = 0
    worst_record_count = 0
    best_reccord = scores[0]
    worst_record = scores[0]
    for i in range(1,len(scores)):
        if(scores[i] > best_reccord):
            best_reccord = scores[i]
            best_reccord_count += 1
        if(scores[i] < worst_record):
            worst_record = scores[i]
            worst_record_count += 1
    return best_reccord_count,worst_record_count
    # Write your code here


n = int(input().strip())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)
print(result)


