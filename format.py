import json
from collections import defaultdict

def extract_key_value_pairs(file_path):
# 用于存储提取出的键值对
    pairs = {}
    # 读取文件中的每一行并解析为Python对象
    with open(file_path, "r") as f:
        for line in f:
            try:
                data = json.loads(line)
                # 提取每个对象中的键值对
                if type(data) == list:
                    data = data[0]
                if data != None:
                    # 递归函数，用于处理嵌套结构
                    def process_object(obj):
                        if isinstance(obj, dict):
                            for key, value in obj.items():
                                # 如果值是一个嵌套结构，则递归处理
                                if isinstance(value, (dict, list)):
                                    process_object(value)
                                else:
                                    # 否则将键值对添加到字典中
                                    if key in pairs:
                                        pairs[key].add(value)
                                    else:
                                        pairs[key] = {value}

                        elif isinstance(obj, list):
                            for item in obj:
                                process_object(item)
                    # 处理JSON对象
                    process_object(data)
            except json.decoder.JSONDecodeError:
                # 如果遇到JSONDecodeError异常，说明该行数据不符合JSON格式，跳过该行数据继续读取下一行数据
                continue
    return pairs

if __name__ == "__main__":
    pairs = extract_key_value_pairs("/root/REST_Go/RestTestGen/output/response_bodies.txt")
    with open("result.json", "w") as f:
        json.dump({key: list(values) for key, values in pairs.items()}, f)
