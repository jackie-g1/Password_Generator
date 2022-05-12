import random

char = """"1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'\()*+,-./:;<=>?@"""
num_of_pass = int(input("Hello. Welcome to the random password generator. How many passwords would you like? "))
len_of_pass = int(input("Great. How long would you like your password? "))

if num_of_pass <= 0 or len_of_pass <= 0:
    print("Unable to produce a password with current inputs. Goodbye.")
else:
    print('\nHere are your passwords: ')
    for i in range(num_of_pass):
        passwords = ''
        for j in range(len_of_pass):
            passwords += random.choice(char)
        print(passwords)

