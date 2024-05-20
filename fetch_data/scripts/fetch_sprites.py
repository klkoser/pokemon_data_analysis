import pokebase as pb
import json
import os
import requests

# Function to fetch sprite URLs using pokebase and handle potential errors
def fetch_sprite_data(pokemon_id):
    sprite_resources = {}
    try:
        sprite_resources["front_default"] = pb.SpriteResource('pokemon', pokemon_id).url
    except requests.exceptions.HTTPError:
        sprite_resources["front_default"] = None
    
    try:
        sprite_resources["back_default"] = pb.SpriteResource('pokemon', pokemon_id, back=True).url
    except requests.exceptions.HTTPError:
        sprite_resources["back_default"] = None

    try:
        sprite_resources["front_shiny"] = pb.SpriteResource('pokemon', pokemon_id, other=True).url
    except requests.exceptions.HTTPError:
        sprite_resources["front_shiny"] = None
    
    try:
        sprite_resources["back_shiny"] = pb.SpriteResource('pokemon', pokemon_id, other=True, back=True).url
    except requests.exceptions.HTTPError:
        sprite_resources["back_shiny"] = None
    
    try:
        sprite_resources["official_artwork"] = pb.SpriteResource('pokemon', pokemon_id, other=True, official_artwork=True).url
    except requests.exceptions.HTTPError:
        sprite_resources["official_artwork"] = None
    
    return sprite_resources

# Directory to save sprite data and images
sprite_json_dir = "../data/sprites/sprite_json/"
sprite_images_dir = "../data/sprites/sprite_images/"
os.makedirs(sprite_json_dir, exist_ok=True)
os.makedirs(sprite_images_dir, exist_ok=True)

# Function to download and save an image from a URL
def download_image(url, path):
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            with open(path, 'wb') as file:
                file.write(response.content)

# Fetch and save sprite data and images for the first 150 Pokémon
for pokemon_id in range(1, 1302):
    data = fetch_sprite_data(pokemon_id)
    with open(f"{sprite_json_dir}/{pokemon_id}.json", 'w') as file:
        json.dump(data, file, indent=4)
    
    # Download and save each sprite image
    for sprite_type, url in data.items():
        if url:
            image_path = os.path.join(sprite_images_dir, f"{pokemon_id}_{sprite_type}.png")
            download_image(url, image_path)

print("Sprite data fetching and saving complete.")
