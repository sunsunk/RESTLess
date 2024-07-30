import json
import os

# Specify the path to the folder you want to find
folder_path = "./giteegitea-20230427034650308/Report/NominalFuzzer"

# Define the target response status code
target_code = [200,201,202,203,204,205]

# Stores a list of responseBody values that match the criteria
response_body_list = []
falg = 1
# Iterate through all files in a folder
for filename in os.listdir(folder_path):
    # Make sure the file is in JSON format
    if filename.endswith(".json"):
        # Open the file and parse the JSON data
        # print(":"+filename)
        with open(os.path.join(folder_path, filename), "r") as f:
            data = json.load(f)
            # Check if the response status code is the target value
            if "testInteractions" in data and "responseStatusCode" in data["testInteractions"][0] and data["testInteractions"][0]["responseStatusCode"].get("code") in target_code:
                # Extract the responseBody value
                response_body = data.get("testInteractions")[0].get("responseBody")
                if response_body != "[]\n" and response_body:
                    response_body_list.append(response_body)
        

#Write a list of responseBody values to a text file
with open("./response_bodies.txt", "w") as f:
    f.write("\n".join(response_body_list))
