import random

print("Welcome to Password Generator")


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%&*().,?0123456789"

number = input("How many passwords do you want to generate: ")
number = int(number)

length = input('Your password length: ')
length = int(length)

print()
print("Here are yours passwords:")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    
    print(passwords)