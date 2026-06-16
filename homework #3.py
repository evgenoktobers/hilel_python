#task 1 Найпростіший калькулятор

first_number = int(input( "введіть перше число: "))
second_number = int(input( "введіть друге число: "))
math_action = input( "зазначте математичну дію: ")

if math_action == "-":
    print(first_number - second_number)
elif math_action == "+":
    print(first_number + second_number)
elif math_action == "*":
    print(first_number * second_number)
elif math_action == "/":
    if second_number == 0:
        print("на нуль ділити поки що не можна")
    else: print(first_number / second_number)
else: print("неправильне значення")