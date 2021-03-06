# import requests
#
# pokemon_id = 1
#
# response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
# pokemon_data = response.json()
#
# print(pokemon_data['name'])


# import requests
# import random
#
# pokemon_id = random.choice(range(1, 152))
#
# response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
# # Converts from JavaScript Object Notation into Python lists and dictionaries
# pokemon_data = response.json()
#
# print(f"You got pokemon number {pokemon_data['id']}, {pokemon_data['name'].capitalize()}!")
# print(f"Height: {pokemon_data['height']} - Weight: {pokemon_data['weight']}")
#
# for type_data in pokemon_data['types']:
#     print(type_data['type']['name'])


import requests
import random

pokemon_id = random.choice(range(1, 152))

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
# Converts from JavaScript Object Notation into Python lists and dictionaries
pokemon_data = response.json()

print(f"You got pokemon number {pokemon_data['id']}, {pokemon_data['name'].capitalize()}!")
print(f"Height: {pokemon_data['height']} • Weight: {pokemon_data['weight']}")

pokemon_types = []
for type_data in pokemon_data['types']:
    pokemon_types.append(type_data['type']['name'])

print(f"Type(s): {' and '.join(pokemon_types)}")