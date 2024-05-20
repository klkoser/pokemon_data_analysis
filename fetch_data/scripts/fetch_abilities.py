# scripts/pokebase_helper.py
import requests

def pokebase_to_dict(obj):
    if isinstance(obj, list):
        return [pokebase_to_dict(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: pokebase_to_dict(v) for k, v in obj.items()}
    elif hasattr(obj, '__dict__'):
        return {k: pokebase_to_dict(v) for k, v in obj.__dict__.items() if not k.startswith('_')}
    else:
        return obj

def get_total_count(resource):
    url = f"https://pokeapi.co/api/v2/{resource}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['count']
    else:
        response.raise_for_status()
