#RANDOM PASSWORD GENERATOR

import random
import string

pass_length = 8

pass_values = string.ascii_letters +string.digits + string.punctuation

password =""

for i in range(pass_length):
    password += random.choice(pass_values)

print("\nYour Random Password is =", password)