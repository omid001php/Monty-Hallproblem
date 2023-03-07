import random

# Function to simulate the Monty Hall problem
def monty_hall(switch):
    # Assign one of the doors to have the prize at random
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)

    # Contestant chooses a door at random
    chosen_door = random.randint(0, 2)

    # Host reveals one of the doors with a goat behind it
    for i in range(3):
        if i != chosen_door and doors[i] == "goat":
            revealed_door = i
            break

    # If the contestant chooses to switch, choose the other unopened door
    if switch:
        for i in range(3):
            if i != chosen_door and i != revealed_door:
                chosen_door = i
                break

    # Return True if the contestant wins the car, False otherwise
    return doors[chosen_door] == "car"

# Simulate the Monty Hall problem 10000 times and count how many times switching wins
switch_wins = 0
for i in range(10000):
    if monty_hall(True):
        switch_wins += 1

# Print the probability of winning by switching
print("Probability of winning by switching:", switch_wins/10000)
