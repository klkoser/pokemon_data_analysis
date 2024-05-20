import pokebase as pb
import json
import os
import requests
from pokebase_helper import pokebase_to_dict, get_total_count

# Directory to save gender data
gender_json_dir = "../data/pokemon/gender/"
os.makedirs(gender_json_dir, exist_ok=True)

# Get the total number of genders
total_genders = get_total_count('gender')

# Fetch and save gender data for all genders
for gender_id in range(1, total_genders + 1):
    try:
        gender = pb.gender(gender_id)
        gender_data = pokebase_to_dict(gender)
        with open(f"{gender_json_dir}/gender_{gender_id}.json", 'w') as file:
            json.dump(gender_data, file, indent=4)
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching gender {gender_id}: {e}")

print("Gender data fetching and saving complete.")