import json

# 读取原始文档A
with open('gitea_test.json', 'r', encoding='utf-8') as f:
    original_document = json.load(f)

# 读取字典文档B
with open('test.json', 'r', encoding='utf-8') as f:
    dictionary_document = json.load(f)

# 遍历原始文档A中的 API
for path, api in original_document['paths'].items():
    # 遍历 API 中的参数
    for method, operation in api.items():
        parameters = operation.get('parameters', [])
        for parameter in parameters:
            # 如果参数名在字典文档B中
            if parameter['name'] in dictionary_document:
                # 如果参数的 "enum" 不存在，创建 "enum" 并将字典文档B中对应的参数值添加到 "enum" 中
                if 'enum' not in parameter:
                    parameter['enum'] = [dictionary_document[parameter['name']]]
                else:
                    # 如果参数的 "enum" 已经存在，在 "enum" 中添加字典文档B中对应的参数值
                    existing_values_set = set(parameter['enum'])
                    new_values_set = set()
                    if isinstance(dictionary_document[parameter['name']], list):
                        new_values_set.update(dictionary_document[parameter['name']])
                    else:
                        new_values_set.add(dictionary_document[parameter['name']])
                    if new_values_set.difference(existing_values_set):
                        parameter['enum'] = list(existing_values_set.union(new_values_set))

# 输出修改后的原始文档A
print(json.dumps(original_document, indent=2))