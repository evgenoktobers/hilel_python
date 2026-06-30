number = int(input("введіть ваше число: "))

while number > 9:
    result = 1

    while number > 0:
        num = number % 10
        result = result * num
        number = number // 10


    number = result
    print(result)

print("Число має бути більше 9")