import json 
import os
DB_FILE = "data/database.json"
def load_data():
     if not os.path.exists(DB_FILE): 
        return {"users": []} 
     try: 
        with open(DB_FILE, "r") as file: return json.load(file)
     
     except json.JSONDecodeError:
        return {"users": []} 
def save_data(data):
    with open(DB_FILE, "w") as file:
     json.dump(data, file, indent=4)