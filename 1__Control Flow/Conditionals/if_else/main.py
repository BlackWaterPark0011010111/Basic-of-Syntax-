import os

def find_config_files(folder):
    """Scans directory for config files"""
    for item in os.listdir(folder):
        if item.endswith('.config'):
            print(f"Config found: {item}")
            break
        print(f"Checking {item}...")
    else:
        print("No configs found, creating default")

# Test runs
find_config_files('/etc/')
find_config_files('/temp/')

def get_valid_age():
    """Keeps asking until valid age entered"""
    while 1:  # Infinite loop until valid
        try:
            years = int(input("Enter your age: "))
            if years < 0:
                raise ValueError("Age can't be negative!")
        except ValueError as error:
            print(f"Invalid: {error}. Try again")
            continue
        else:
            print("Age accepted!")
            return years
        finally:
            print("Thanks for responding!")

# Test
age = get_valid_age()
print(f"You're {age} years old")

from random import randint
"""Number Guessing Game (with attempt tracking)"""
def play_guess_game():
    secret_num = randint(1, 10)
    tries = 3
    
    print("Guess number (1-10). You get 3 tries!")
    
    for attempt in range(tries):
        guess = int(input(f"Attempt {attempt+1}: "))
        if guess == secret_num:
            print("You won! Perfect!")
            break
        print("Wrong guess!")
    else:
        print(f"Game over! Number was: {secret_num}")

play_guess_game()