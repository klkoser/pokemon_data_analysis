import pokebase as pb
import json
import os
import requests
from pokebase_helper import pokebase_to_dict, get_total_count

# Directory to save color data
color_json_dir = "../data/pokemon/colors/"
os.makedirs(color_json_dir, exist_ok=True)

# Get the total number of colors
total_colors = get_total_count('pokemon-color')

# Fetch and save color data for all colors
for color_id in range(1, total_colors + 1):
    try:
        color = pb.pokemon_color(color_id)
        color_data = pokebase_to_dict(color)
        with open(f"{color_json_dir}/color_{color_id}.json", 'w') as file:
            json.dump(color_data, file, indent=4)
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching color {color_id}: {e}")

print("Color data fetching and saving complete.")