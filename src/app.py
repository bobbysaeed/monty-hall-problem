import random

doors = [1, 2, 3]
prizes = ['goat', 'car', 'goat']
random.shuffle(prizes)
choices = dict(zip(doors, prizes))

# Get valid first choice
while True:
    try:
        user_choice = int(input('Please choose a door from 1 to 3: '))
        if user_choice in doors:
            break
        print("Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Monty opens a random goat door that's not the user's choice
goat_doors = [d for d in doors if choices[d] == 'goat' and d != user_choice]
monty_opens = random.choice(goat_doors)
print(f"Monty opens door {monty_opens} — it's a goat!")

# Ask player if they want to switch
while True:
    second_chance = input("Do you want to change your choice? (y/n): ").strip().lower()
    if second_chance in ('y', 'n'):
        break
    print("Please enter 'y' or 'n'.")

if second_chance == 'y':
    # Switch to the only remaining unopened door
    final_choice = [d for d in doors if d != user_choice and d != monty_opens][0]
else:
    final_choice = user_choice

# Reveal prize
print(f"The prize behind door {final_choice} is {choices[final_choice]}!")
