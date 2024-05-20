import pokebase as pb
import json
import os
import requests
from pokebase_helper import pokebase_to_dict, get_total_count

# Directory to save stat data
stat_json_dir = "../data/pokemon/stats/"
os.makedirs(stat_json_dir, exist_ok=True)

# Get the total number of stats
total_stats = get_total_count('stat')

# Fetch and save stat data for all stats
for stat_id in range(1, total_stats + 1):
    try:
        stat = pb.stat(stat_id)
        stat_data = pokebase_to_dict(stat)
        with open(f"{stat_json_dir}/stat_{stat_id}.json", 'w') as file:
            json.dump(stat_data, file, indent=4)
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching stat {stat_id}: {e}")

print("Stat data fetching and saving complete.")