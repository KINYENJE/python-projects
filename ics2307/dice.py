import random
from collections import Counter

# Simulate rolling a dice 1000 times
rolls = [random.random() * 6 // 1 + 1 for _ in range(1000)]
print(f"this is the number of rolls {rolls} \n")

# Count the frequency of each face
counter = Counter(rolls)
print(f"This is the {counter} \n")
print(f"This is the {counter.items()} \n")


# Calculate the percentage occurrence of each face
total_rolls = len(rolls)
print(f"This is the total number of rolls {total_rolls} \n")

# Calculate the percentage occurrence of each face
percentages = {face: count / total_rolls * 100 for face, count in counter.items()}
print(f"This is the percentage {percentages} \n")

# Print the table header
print("Face\tFrequency\tPercentage")
print("-" * 30) # Print a line of 30 dashes

# Print each face, frequency, and percentage
for face in range(1, 7):
    frequency = counter.get(face, 0)
    percentage = percentages.get(face, 0)
    print(f"{face}\t\t\t{frequency}\t\t\t\t{percentage:.2f}%")
