import pokebase as pb
import json
import os
import requests
from pokebase_helper import pokebase_to_dict, get_total_count

# Directory to save shape data
shape_json_dir = "../data/pokemon/shapes/"
os.makedirs(shape_json_dir, exist_ok=True)

# Get the total number of shapes
total_shapes = get_total_count('pokemon-shape')

# Fetch and save shape data for all shapes
for shape_id in range(1, total_shapes + 1):
    try:
        shape = pb.pokemon_shape(shape_id)
        shape_data = pokebase_to_dict(shape)
        with open(f"{shape_json_dir}/shape_{shape_id}.json", 'w') as file:
            json.dump(shape_data, file, indent=4)
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching shape {shape_id}: {e}")

print("Shape data fetching and saving complete.")