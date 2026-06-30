import string

text = input("Введіть рядок")

words = text.split()

result = ""

for word in words:
    clean_word = ""
    for letter in word:
        if letter not in string.punctuation:
            clean_word = clean_word + letter

    if len(clean_word) > 0:
        first_letter = clean_word[0].upper()
        rest_letters = clean_word[1:].lower()
        new_word = first_letter + rest_letters
        result = result + new_word

hashtag = "#" + result

if len(hashtag) > 140:
    hashtag = hashtag[0:140]

print(hashtag)