import pokebase as pb
import json
import os
import requests
from pokebase_helper import pokebase_to_dict, get_total_count

# Directory to save type data
type_json_dir = "../data/pokemon/types/"
os.makedirs(type_json_dir, exist_ok=True)

# Get the total number of types
total_types = get_total_count('type')

# Fetch and save type data for all types
for type_id in range(1, total_types + 1):
    try:
        type_ = pb.type_(type_id)
        type_data = pokebase_to_dict(type_)
        with open(f"{type_json_dir}/type_{type_id}.json", 'w') as file:
            json.dump(type_data, file, indent=4)
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching type {type_id}: {e}")

print("Type data fetching and saving complete.")
