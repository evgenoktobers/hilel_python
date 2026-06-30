import string
import keyword

userInput = input("Введіть рядок: ")

getValue = True

if len(userInput) == 0:
    getValue = False

elif userInput[0].isdigit():
    getValue = False

else:
    if userInput != userInput.lower():
        getValue = False

    underscoreCheck = string.punctuation.replace("_", "")
    for ch in userInput:
        if ch == " " or ch in underscoreCheck:
            getValue = False
            break

    if "__" in userInput:
        getValue = False

    if userInput in keyword.kwlist:
        getValue = False

print(getValue)