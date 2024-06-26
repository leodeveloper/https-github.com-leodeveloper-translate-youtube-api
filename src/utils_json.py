import os
import json
from src.utils_dycrypt import decrypt_string

from dotenv import load_dotenv
load_dotenv()

key=os.getenv("encryptkey")

# Function to read JSON data from a file
def read_json_from_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to find an item by source value
def find_by_source(data, source_value):
    for item in data:
        if item['source'] == source_value:
            return item
    return None

def get_json(source):
    # Path to the JSON file
    json_file_path = './combined_extracted_data_youtubelink.json'

    # Read JSON data from the file
    data = read_json_from_file(json_file_path)

    # Example source value to find
    source_to_find = source
    result = find_by_source(data, source_to_find)

    # Print the result
    if result:
        #print(f"Found item: {result}")
        return result
    else:
        #print(f"No item found with source '{source_to_find}'")
        return None
