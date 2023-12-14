import json
import os

def txt_to_json(txt_filename, json_filename):
    with open(txt_filename, 'r') as txt_file:
        lines = txt_file.readlines()

    data = {'objects': []}

    for line in lines:
        # 假设每行的格式是 "class_name x_center y_center width height"
        parts = line.strip().split()
        class_name, x_center, y_center, width, height = parts

        # 转换为 JSON 数据格式
        obj_data = {
            'class_name': class_name,
            'bbox': {
                'x_center': float(x_center),
                'y_center': float(y_center),
                'width': float(width),
                'height': float(height)
            }
        }

        data['objects'].append(obj_data)

    # 将数据保存为 JSON 文件
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def batch_convert_txt_to_json(txt_folder, json_folder):
    if not os.path.exists(json_folder):
        os.makedirs(json_folder)

    for txt_filename in os.listdir(txt_folder):
        if txt_filename.endswith('.txt'):
            json_filename = txt_filename.replace('.txt', '.json')
            txt_path = os.path.join(txt_folder, txt_filename)
            json_path = os.path.join(json_folder, json_filename)

            txt_to_json(txt_path, json_path)




# 指定你的 txt 文件夹和 json 存储文件夹
txt_folder_path = 'D:/0.Data/pineapple/pineapple/pineapple_weed_yolo/txt'
json_folder_path = 'D:/0.Data/pineapple/pineapple/multi_line_weed_dataset/detection-weed'

batch_convert_txt_to_json(txt_folder_path, json_folder_path)
