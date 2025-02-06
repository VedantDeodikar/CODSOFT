import random
import string
def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(all_characters)
    return password
print("Welcome to the Password Generator!")
length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print("Your generated password is: " + password)
