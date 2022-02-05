from collections import Counter

def checkMagazine(magazine, note):
    if (Counter(note)-Counter(magazine)=={}):
        return "Yes"
    return "No"

first_multiple_input = input().rstrip().split()

m = int(first_multiple_input[0])

n = int(first_multiple_input[1])

magazine = input().rstrip().split()

note = input().rstrip().split()

print(checkMagazine(magazine, note))

