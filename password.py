import random

choice = int(input("Введите длину пароля (не более 25 символов): "))

if choice > 25:
    print("Ошибка: длина пароля не должна превышать 25 символов.")
    exit()

choicenumchr = input("Делать ли фильтрацию по цифрам (y, n): ")

if choicenumchr.lower() == "y":
    choicenumchr = True
elif choicenumchr.lower() == "n":
    choicenumchr = False
else:
    print("Вы можете ввести только^_* y или n.")
    exit()

password = ""