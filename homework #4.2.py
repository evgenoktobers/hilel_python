#Знайти суму елементів із парними індексами
valuesList = [0, 0, 1, 0, 3, 0, 12, 0, 4, 2, 0]

if len(valuesList) > 0:
    evenNumbers = 0

    for i in range(len(valuesList)):
        if i % 2 == 0:
            evenNumbers += valuesList[i]

    print(evenNumbers)

    multiplyValue = evenNumbers * valuesList[-1]

    print(multiplyValue)
else:
    multiplyValue = 0
    print(multiplyValue)