while True:
    first_number = int(input("Введіть перше число: "))
    second_number = int(input("Введіть друге число: "))
    math_action = input("Зазначте математичну дію: ")

    if math_action == "-":
        print(first_number - second_number)
    elif math_action == "+":
        print(first_number + second_number)
    elif math_action == "*":
        print(first_number * second_number)
    elif math_action == "/":
        if second_number == 0:
            print("На нуль ділити поки що не можна")
        else:
            print(first_number / second_number)
    else:
        print("Неправильне значення")

    continue_calc = input("Бажаєте продовжити? (y - так, інше - вийти): ")

    if continue_calc != "y":
        print("Дякуємо за користування нашим застосунком. Всього найкращого.")
break