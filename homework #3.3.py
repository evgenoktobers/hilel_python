listToSplit = [1, 2, 3, 4, 5]

count = sum(1 for _ in listToSplit)

if count == 0:
    result = [[], []]
elif count % 2 == 0:
    mid = count // 2
    result = [listToSplit[:mid], listToSplit[mid:]]
else:
    mid = count // 2 + 1
    result = [listToSplit[:mid], listToSplit[mid:]]

print(result)