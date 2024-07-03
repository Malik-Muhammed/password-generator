import random

# List of numbers to choose from
number = ["1", "2", "3" "4","5", "6", "7", "8", "9" , "0"]

# List of uppercase letters to choose from
alphabet = ["A", "B", "C", "D", "E",  "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q", "R" 
           "S", "T", "U","V", "W", "X", "Y", "Z"]

# List of symbols to choose from
symbols = ["@", "!", "(", ")","_" , "#", "[", "]", "%", "$", "&", "*"]

print("WELCOME TO PASSWORD GENERATOR")

# Get user input for password composition
num_of_small_letter = int(input("How many small letters would you like in your password?"))
num_of_cap_letter = int(input("How many capital letters would you like in your password?"))
num_of_numbers = int(input("How many numbers would you like in your password?"))
num_of_symbols = int(input("How many symbols would you like in your password?"))

# Initialize empty password string
password=""

# Add lowercase letters to password
for n in range(1, num_of_small_letter + 1):
    password += (random.choice(alphabet)).lower()

# Add uppercase letters to password
for n in range(1, num_of_cap_letter + 1):
    password += (random.choice(alphabet))

# Add numbers to password
for n in range(1, num_of_numbers + 1):
    password  += (random.choice(number))

# Add symbols to password
for n in range(1, num_of_symbols + 1):
    password += (random.choice(symbols))

# Print the initial password (characters in order of type)
print(password)

# Convert password string to list for shuffling
password = list(password)

# Shuffle the characters in the password
random.shuffle(password)

# Join the shuffled characters back into a string
randomized_password = "".join(password)

# Print the final randomized password
print(randomized_password)