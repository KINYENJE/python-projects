import random
from collections import Counter

def roll_dice():
    return random.random()


def get_face(random_number):
    if random_number < 1/6:
        return 1
    elif 1/6 <= random_number < 2/6:
        return 2
    elif 2/6 <= random_number < 3/6:
        return 3
    elif 3/6 <=  random_number < 4/6:
        return 4
    elif 4/6 <= random_number < 5/6:
        return 5
    else:
        return 6
    
rolls = [get_face(roll_dice()) for _ in range(1000)] # rolls are integers between 1 and 6
print(f"this is the number of rolls {rolls} \n") 

# Count the frequency of each face
counter = Counter(rolls)
print(f"This is the {counter} \n")
print(f"This is the {counter.items()} \n")




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
