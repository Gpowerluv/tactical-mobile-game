import os, json
CACHE_FILE = 'local_cache.json'
def save_cache(data):
    with open(CACHE_FILE, 'w') as f:
        json.dump(data, f)
def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {}
