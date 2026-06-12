#task 1 Квадрат числа

# input_number = int(input( "введіть число: "))
#
# square = input_number ** 2
#
# print(square)

#--------------------------------------------------------------
#task 2 “Середнє трьох чисел”

# first_number = int(input( "введіть перше число: "))
# second_number = int(input( "введіть друге число: "))
# third_number = int(input( "введіть третє число: "))
#
# avg = int(first_number+second_number+third_number) / 3
#
# print(avg)

#--------------------------------------------------------------
#task 3 “Перетворення хвилин у години”

# minutes = int(input("введіть кількість хвилин: "))
#
# hours = minutes // 60
# leftowers = minutes % 60
#
# print(f"ваш результат, {hours} годин і {leftowers} хвилин")

#--------------------------------------------------------------
#task 4 “Розрахунок знижки”

# price = int(input("введіть ціну: "))
# discount = int(input("введіть знижку (%): "))
#
# final_price = price - price / 100 * discount
#
# print(final_price)

#--------------------------------------------------------------
#task5 “Остання цифра числа”

# number = int(input("введіть число: "))
# result_number = number % 10 # 6
# print(result_number)

#--------------------------------------------------------------
#task6 “Периметр прямокутника”
# length = int(input("введіть довжину: "))
# width = int(input("введіть ширину: "))
#
# result = length*2 + width*2
#
# print(f"Периметр прямокутника {result}")

#--------------------------------------------------------------
#task7 Виведення числа в стовпчик
# number = int(input("введіть чотиризначне число: "))
#
# n1 = number // 1000
# n2 = number // 100 % 10
# n3 = number % 100 // 10
# n4 = number % 10
#
# print(n1)
# print(n2)
# print(n3)
# print(n4)