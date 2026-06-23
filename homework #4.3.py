#Список із 3 елементів

import random

randomList = random.randint(3, 10)

values = [random.randint(1, 100) for _ in range(randomList)]

print(randomList)
print(values)

finalValues = [values[0], values[2], values[-2]]

print(finalValues)