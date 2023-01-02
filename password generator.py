import random

print("Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
number = input("Enter how many passwords to generate: ")
number = int(number)
length = input("Enter the password length: ")
length = int(length)
for i in range(number):
    passwd = ''
    for c in range(length):
        passwd += random.choice(chars)
    print(passwd)
