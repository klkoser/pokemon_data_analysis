import pokebase as pb
import json
import os
import requests
from pokebase_helper import pokebase_to_dict, get_total_count

# Directory to save characteristic data
characteristic_json_dir = "../data/pokemon/characteristics/"
os.makedirs(characteristic_json_dir, exist_ok=True)

# Get the total number of characteristics
total_characteristics = get_total_count('characteristic')

# Fetch and save characteristic data for all characteristics
for characteristic_id in range(1, total_characteristics + 1):
    try:
        characteristic = pb.characteristic(characteristic_id)
        characteristic_data = pokebase_to_dict(characteristic)
        with open(f"{characteristic_json_dir}/characteristic_{characteristic_id}.json", 'w') as file:
            json.dump(characteristic_data, file, indent=4)
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching characteristic {characteristic_id}: {e}")

print("Characteristic data fetching and saving complete.")