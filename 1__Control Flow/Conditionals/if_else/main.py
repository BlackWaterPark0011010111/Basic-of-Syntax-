import os

# looking for config files in folder
def find_config_files(folder):
    for thing in os.listdir(folder):
        if thing.endswith('.config'):
            print(f"FOUND CONFIG FILE: {thing}")
            break
        print(f"looking at {thing}...")
    else:
        print("NO CONFIGS FOUND, MAKING NEW ONE")

find_config_files('/etc/')
find_config_files('/temp/')


# asking for age with checks
def get_age():
    while True:
        try:
            age = int(input("ENTER YOUR AGE: "))
            if age < 0:
                raise ValueError("AGE CANT BE NEGATIVE DUDE")
        except ValueError as err:
            print(f"ERROR: {err}. TRY AGAIN PLS")
            continue
        else:
            print("AGE OK!")
            return age
        finally:
            print("THANKS FOR ANSWERING")

user_age = get_age()
print(f"you are {user_age} years old")


# getting api stuff
import requests

def grab_api_info(url):
    try:
        r = requests.get(url, timeout=3)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"API PROBLEM: {e}")
    else:
        print("GOT DATA FROM API!")
        return r.json()
    finally:
        print("DONE WITH API STUFF")

stuff = grab_api_info("https://api.test.com/v1/data")
if stuff:
    print(f"got {len(stuff)} things")


# number guessing fun
from random import randint

def number_game():
    secret = randint(1, 10)
    guesses = 3
    
    print("GUESS NUMBER 1-10. YOU GET 3 TRIES!")
    
    for try_num in range(guesses):
        guess = int(input(f"YOUR GUESS {try_num+1}: "))
        if guess == secret:
            print("YOU GOT IT! NICE!")
            break
        print("WRONG!")
    else:
        print(f"GAME OVER! IT WAS {secret}")

number_game()