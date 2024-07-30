import json
from collections import defaultdict

def extract_key_value_pairs(file_path):
    # Used to store the extracted key-value pairs
    pairs = {}
    # Read each line in the file and parse it as a Python object
    with open(file_path, "r") as f:
        for line in f:
            try:
                data = json.loads(line)
                # Extract key-value pairs from each object
                if type(data) == list:
                    data = data[0]
                if data != None:
                    # Recursive function to handle nested structures
                    def process_object(obj):
                        if isinstance(obj, dict):
                            for key, value in obj.items():
                                # If the value is a nested structure, recursively process it
                                if isinstance(value, (dict, list)):
                                    process_object(value)
                                else:
                                    # Otherwise, add the key-value pair to the dictionary
                                    if key in pairs:
                                        pairs[key].add(value)
                                    else:
                                        pairs[key] = {value}

                        elif isinstance(obj, list):
                            for item in obj:
                                process_object(item)
                    # Process the JSON object
                    process_object(data)
            except json.decoder.JSONDecodeError:
                # If a JSONDecodeError exception is encountered, it means that the line data does not conform to JSON format, skip the line and continue reading the next line
                continue
    return pairs

