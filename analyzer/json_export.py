import json

def to_json(data, filepath):
    """Export data to a JSON file."""
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def from_json(filepath):
    """Import data from a JSON file."""
    with open(filepath, 'r') as json_file:
        return json.load(json_file)
