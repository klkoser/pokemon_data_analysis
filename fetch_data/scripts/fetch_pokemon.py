import pokebase as pb
import json
import os
import requests
from pokebase_helper import pokebase_to_dict, get_total_count

# Directory to save pokemon data
pokemon_json_dir = "../data/pokemon/pokemon/"
os.makedirs(pokemon_json_dir, exist_ok=True)

# Get the total number of pokemon
total_pokemon = get_total_count('pokemon')

# Fetch and save pokemon data for all pokemon
for pokemon_id in range(1, total_pokemon + 1):
    try:
        pokemon = pb.pokemon(pokemon_id)
        pokemon_data = pokebase_to_dict(pokemon)
        with open(f"{pokemon_json_dir}/pokemon_{pokemon_id}.json", 'w') as file:
            json.dump(pokemon_data, file, indent=4)
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching pokemon {pokemon_id}: {e}")

print("Pokemon data fetching and saving complete.")