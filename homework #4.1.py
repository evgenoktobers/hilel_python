#Перемістити всі нулі до кінця списку

valuesList = [0, 1, 0, 3, 0, 12, 0, 5, 0]
result = []
zeros = []

for item in valuesList:
    if item == 0:
        zeros.append(item)
    else:
        result.append(item)

result = result + zeros

print(result)