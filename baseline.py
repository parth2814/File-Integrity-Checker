import os
import hashlib
import json
from datetime import datetime

def calculate_file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def create_baseline(directory, database_file='baseline.json'):
    baseline = {}
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_hash = calculate_file_hash(filepath)
            relative_path = os.path.relpath(filepath, directory)
            baseline[relative_path] = {
                'hash': file_hash,
                'last_modified': datetime.now().isoformat()
            }
    
    with open(database_file, 'w') as f:
        json.dump(baseline, f, indent=4)
    
    print(f"Baseline created and saved to {database_file}")