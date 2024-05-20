import pokebase as pb
import json
import os

# Directory to save generation data
generation_json_dir = "../data/generations/"
os.makedirs(generation_json_dir, exist_ok=True)

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

# Fetch and save generation data for all generations
for generation_id in range(1, 9):  # Update the range based on the total number of generations available
    generation = pb.generation(generation_id)
    generation_data = pokebase_to_dict(generation)
    with open(f"{generation_json_dir}/generation_{generation_id}.json", 'w') as file:
        json.dump(generation_data, file, indent=4)

print("Generation data fetching and saving complete.")
