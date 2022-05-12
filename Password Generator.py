import random

num_of_pass = int(input("Hello. Welcome to the random password generator. How many passwords would you like? "))
if num_of_pass > 0:
    len_of_pass = int(input("Great. How long would you like your password? "))
else:
    print("Got it. Goodbye.")

char = """"1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'\()*+,-./:;<=>?@"""

print('\nHere are your passwords: ')
for pwd in range(num_of_pass):
    passwords = ''
    for c in range(len_of_pass):
        passwords += random.choice(char)
    print(passwords)
