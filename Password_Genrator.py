#Task3 Password Generator

import random
import string

def generate_password(length):
    # Define the characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Prompt the user to specify the desired length of the password
length = int(input("Enter the desired length of the password: "))

# Generate the password
password = generate_password(length)

# Display the generated password
print("Generated Password:", password)
