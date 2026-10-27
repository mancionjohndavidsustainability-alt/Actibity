import requests
import random

pokemon = random.randint(1,20)
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
response = requests.get(url)
data = response.json()

poke_name = data["name"].lower()
poke_h = data["height"]
poke_w = data["weight"]

reveled_char = 1
guessed_correctly = False

while reveled_char <= len(poke_name):
    hint_name = poke_name[:reveled_char]
    print(hint_name)
    print(f"Pokemon Weight: {poke_w}")
    print(f"Pokemon Height: {poke_h}")
    
    guess_input = input("Your Guess: ").lower()
    
    if guess_input == poke_name:
        print(f"You've Guessed the Pokemon! it was: {poke_name}")
        guessed_correctly = True
        break
    else:
        print("Wrong Guess!")
        reveled_char += 1

if not guessed_correctly:
    print(f"Out OF Guesses! Pokemon was: {poke_name}")
 