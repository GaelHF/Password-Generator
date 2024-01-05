from random import choice, randint
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

lenght = int(input("Password Lenght : "))
password = ""

for i in range(lenght):
    type = randint(1, 4)
    if type == 1:
        password += str(choice(ascii_lowercase))
    elif type == 2:
        password += str(choice(ascii_uppercase))
    elif type == 3:
        password += str(choice(digits))
    else:
        password += str(choice(punctuation))

print(password)