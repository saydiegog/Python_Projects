import string
import random
import pyclip

chars = string.ascii_letters + string.digits + string.punctuation

length = int(input("Please enter your desired password length: "))
password = ""

for i in range (0, length):
    password = password + random.choice(chars)

pyclip.copy(password)
print(f"Your generated password is {password}. Copied to clipboard!")