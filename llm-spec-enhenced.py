import json
import copy
import os
import openai
import time

## value generation demo
def generate_new_value(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    generated_text = response.choices[0].text.strip()

    return generated_text
def get_completion(prompt, model="gpt-3.5-turbo"):
     messages = [{"role": "user", "content": prompt}]
     response = openai.ChatCompletion.create(
     model=model,
     messages=messages,
     temperature=0, # this is the degree of randomness of the model's output
     )
     return response.choices[0].message["content"]

def generate_new_parameters(json_data):
    
    new_data = {}
#     gptprompt = f"""
#           I now have a json document containing parameter A and parameter value B. Your task now is to
#         1. learn the semantics of parameter value B. \
#         2. Generate 5 random parameter values for parameter A that match the semantics of step 1,and if B is a boolean type value,you just need generate 2 values\
#         3. finally output the generated parameter values as a list.\
#         Special note: I don't need you to tell me how to do this, I just need the list generated in step 3,just a list without any Explanation!\
#         Output example: [value1,value2,...,value5]
#         A:{key}
#         B:{value}
#         """
#     davinciprompt= f"""
#         Please generate a new parameter value that matches the semantics of parameter {value}
#     """
    for key, value in json_data.items():
        prompt = f"""
          I now have a json document containing parameter A and parameter value B. Your task now is to
        1. learn the semantics of parameter value B. \
        2. Generate 5 random parameter values for parameter A that match the semantics of step 1,and if B is a boolean type value,you just need generate 2 values\
        3. finally output the generated parameter values as a list.\
        Special note: I don't need you to tell me how to do this, I just need the list generated in step 3,just a list without any Explanation!\
        Output example: [value1,value2,...,value5]
        A:{key}
        B:{value}
        """
        new_value = get_completion(prompt)
        print("result:"+new_value)
        new_data[key] = new_value
        time.sleep(22)
    return new_data

def read_json_file(file_path):
    with open(file_path, 'r') as f:
        json_data = json.load(f)
    return json_data
def write_json_file(json_data, file_path):
    with open(file_path, 'w') as f:
        json.dump(json_data, f, indent=2)

# Usage:example
json_data = read_json_file("input/merged_file.json")
new_data = generate_new_parameters(json_data)
write_json_file(new_data, "output.json")