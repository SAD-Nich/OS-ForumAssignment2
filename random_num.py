import random

random_numbers = [random.randint(0, 4999) for _ in range(1000)]

with open('input.txt', 'w') as file:
    for num in random_numbers:
        file.write(str(num) + '\n')