import random

# Generate a list of 100 random integers
random_numbers = random.sample(range(1, 1000), 100)

# Write the list to a file
with open('numbers.txt', 'w') as file:
    for number in random_numbers:
        file.write(str(number) + '\n')
