def kangaroo(x1, v1, x2, v2):
    result = 'NO'
    if(v1 == v2):
        result = 'NO'
    else:
        x = (x2 - x1) / (v1 - v2)
        y = (x2 - x1) % (v1 - v2)
        if x < 0:
            result = 'NO'
        elif y == 0:
            result = 'YES'
        else:
            result = 'NO'
    return result
    # Write your code here


first_multiple_input = input().rstrip().split()
x1 = int(first_multiple_input[0])
v1 = int(first_multiple_input[1])
x2 = int(first_multiple_input[2])
v2 = int(first_multiple_input[3])

result = kangaroo(x1, v1, x2, v2)
print(result)
