import random

# Generate 10 random numbers
random_numbers = [random.randint(1, 100) for _ in range(10)]
print("Random numbers:", random_numbers)

# Find the largest random number
largest = max(random_numbers)
print("Largest number:", largest)

# Simulate rolling two dice 100 times and count doubles
doubles_count = 0
for _ in range(100):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 == die2:
        doubles_count += 1

print("Number of doubles in 100 rolls:", doubles_count)
