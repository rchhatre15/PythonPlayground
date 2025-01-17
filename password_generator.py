import random
import string
print("Welcome to the strong password generator!")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))
str_len = letters + symbols + numbers
all_letters = list(string.ascii_letters)
all_symbols = ['@', '#', '$', '%', '^', '&', '*', '_']
all_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password = ""
for i in range(str_len):
    gen = random.randint(0, 2)
    if(gen == 2 and numbers > 0):
        password += all_numbers[random.randint(0, len(all_numbers) - 1)]
        numbers -= 1
    elif(gen == 1 and symbols > 0):
        password += all_symbols[random.randint(0, len(all_symbols) - 1)]
        symbols -= 1
    elif(gen == 0 and letters > 0):
        password += all_letters[random.randint(0, len(all_letters) - 1)]
        letters -= 1
    elif(numbers > 0):
        password += all_numbers[random.randint(0, len(all_numbers))]
        numbers -= 1
    elif(symbols > 0):
        password += all_symbols[random.randint(0, len(all_symbols))]
        symbols -= 1
    else:
        password += all_letters[random.randint(0, len(all_letters))]
        letters -= 1
print(password)
    

