import json

# Read the original document A
with open('gitea_test.json', 'r', encoding='utf-8') as f:
    original_document = json.load(f)

# Read the dictionary document B
with open('test.json', 'r', encoding='utf-8') as f:
    dictionary_document = json.load(f)

# Traverse the APIs in the original document A
for path, api in original_document['paths'].items():
    # Traverse the parameters in the API
    for method, operation in api.items():
        parameters = operation.get('parameters', [])
        for parameter in parameters:
            # If the parameter name is in the dictionary document B
            if parameter['name'] in dictionary_document:
                # If the "enum" of the parameter does not exist, create "enum" and add the corresponding parameter value from the dictionary document B to "enum"
                if 'enum' not in parameter:
                    parameter['enum'] = [dictionary_document[parameter['name']]]
                else:
                    # If the "enum" of the parameter already exists, add the corresponding parameter value from the dictionary document B to "enum"
                    existing_values_set = set(parameter['enum'])
                    new_values_set = set()
                    if isinstance(dictionary_document[parameter['name']], list):
                        new_values_set.update(dictionary_document[parameter['name']])
                    else:
                        new_values_set.add(dictionary_document[parameter['name']])
                    if new_values_set.difference(existing_values_set):
                        parameter['enum'] = list(existing_values_set.union(new_values_set))

# Output the modified original document A
print(json.dumps(original_document, indent=2))
