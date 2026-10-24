import requests
import random
def name_printing(name):
    name_index = 0
    for letter in name:
        letter[name_index]
    name_index+=1
    return " ". join(letter)
pokemon = random.randint(1,20)
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
response = requests.get(url)
data = response.json()

poke_name = data["name"]
poke_h = data["height"]
poke_w = data["weight"]
split_name = name_printing(poke_name)
revealed_name = 1
while revealed_name <= len(poke_name):
    print(f"Pokemon Name: {split_name}")
    print(f"Pokemon Height: {poke_h}")
    print(f"Pokemon Weight: {poke_w}")
    guess = input("Who's that Pokemon?")
 