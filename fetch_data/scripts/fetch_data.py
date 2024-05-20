import pokebase as pb
import json
import os
import requests

# Set up the cache
from pokebase import cache
cache.API_CACHE = cache.Cache(cache_folder="data/cache/")

# Function to fetch sprite data from PokeAPI using pokebase
def fetch_sprite_data(pokemon_id):
    pokemon = pb.pokemon(pokemon_id)
    sprite_urls = {
        "front_default": pokemon.sprites.front_default,
        "back_default": pokemon.sprites.back_default,
        "front_shiny": pokemon.sprites.front_shiny,
        "back_shiny": pokemon.sprites.back_shiny
    }
    return sprite_urls

# Directory to save sprite data and images
sprite_data_dir = "data/sprites/"
sprite_images_dir = "data/sprite_images/"
os.makedirs(sprite_data_dir, exist_ok=True)
os.makedirs(sprite_images_dir, exist_ok=True)

# Function to download and save an image from a URL
def download_image(url, path):
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            with open(path, 'wb') as file:
                file.write(response.content)

# Fetch and save sprite data and images for the first 150 Pokémon
for pokemon_id in range(1, 151):
    data = fetch_sprite_data(pokemon_id)
    with open(f"{sprite_data_dir}/{pokemon_id}.json", 'w') as file:
        json.dump(data, file, indent=4)
    
    # Download and save each sprite image
    for sprite_type, url in data.items():
        if url:
            image_path = os.path.join(sprite_images_dir, f"{pokemon_id}_{sprite_type}.png")
            download_image(url, image_path)

print("Sprite data fetching and saving complete.")

