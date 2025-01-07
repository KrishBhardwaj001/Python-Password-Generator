letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols =  ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "-", ".", "`", "~", "|", "<", ">", "=", "-", "_"]

import random
import string_utils

print("Welcome to the Password Generator!")
password_length = int(input("How many characters do you want in your password?\n"))
remaining_length = password_length
nr_letters = random.randint(1, remaining_length)
remaining_length -= nr_letters
nr_numbers = random.randint(1, remaining_length)
nr_symbols = remaining_length - nr_numbers

password = ""

# Add letters
while nr_letters != 0:
    password += letters[random.randint(0,nr_letters)]
    nr_letters -= 1
# Add numbers
while nr_numbers != 0:
    password += str(numbers[random.randint(0,nr_numbers)])
    nr_numbers -= 1
# Add letters
while nr_symbols != 0:
    password += symbols[random.randint(0,nr_symbols)]
    nr_symbols -= 1

print(f"Your password is: {string_utils.shuffle(password)}")