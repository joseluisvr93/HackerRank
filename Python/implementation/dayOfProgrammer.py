def dayOfProgrammer(year):
    result = ""
    if year == 1918:
        result = "26.09.1918"
    elif (year % 4) == 0:
        if (year % 100) == 0 and year > 2000 and (year % 400):
            result = "13.09."+str(year)
        else:
            result = "12.09."+str(year)
    else:
        result = "13.09."+str(year)
    return result
    # Write your code here

year = int(input().strip())
result = dayOfProgrammer(year)
print(result)

