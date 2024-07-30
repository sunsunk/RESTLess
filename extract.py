import json
import os

# 指定要查找的文件夹路径
folder_path = "./giteegitea-20230427034650308/Report/NominalFuzzer"

# 定义目标响应状态码
target_code = [200,201,202,203,204,205]

# 存储符合条件的responseBody值的列表
response_body_list = []
falg = 1
# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 确保文件是JSON格式
    if filename.endswith(".json"):
        # 打开文件并解析JSON数据
        # print("正在解析:"+filename)
        with open(os.path.join(folder_path, filename), "r") as f:
            data = json.load(f)
            # 检查响应状态码是否为目标值
            if "testInteractions" in data and "responseStatusCode" in data["testInteractions"][0] and data["testInteractions"][0]["responseStatusCode"].get("code") in target_code:
                # 提取responseBody值
                response_body = data.get("testInteractions")[0].get("responseBody")
                if response_body != "[]\n" and response_body:
                    response_body_list.append(response_body)
        

#将responseBody值列表写入文本文件中
with open("./response_bodies.txt", "w") as f:
    f.write("\n".join(response_body_list))