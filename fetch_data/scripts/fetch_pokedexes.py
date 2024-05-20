import pokebase as pb
import json
import os

# Directory to save pokedex data
pokedex_json_dir = "../data/pokedexes/"
os.makedirs(pokedex_json_dir, exist_ok=True)

# Function to convert pokebase object to a dictionary
def pokebase_to_dict(obj):
    if isinstance(obj, list):
        return [pokebase_to_dict(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: pokebase_to_dict(v) for k, v in obj.items()}
    elif hasattr(obj, '__dict__'):
        return {k: pokebase_to_dict(v) for k, v in obj.__dict__.items() if not k.startswith('_')}
    else:
        return obj

# Fetch and save pokedex data for all available pokedexes
pokedex_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]  # Add all known Pokedex IDs

for pokedex_id in pokedex_ids:
    pokedex = pb.pokedex(pokedex_id)
    pokedex_data = pokebase_to_dict(pokedex)
    with open(f"{pokedex_json_dir}/pokedex_{pokedex_id}.json", 'w') as file:
        json.dump(pokedex_data, file, indent=4)

print("Pokedex data fetching and saving complete.")
