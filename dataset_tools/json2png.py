 
from PIL import Image, ImageDraw
import json
import os
# 将json文件转为png文件，需要改标签，input，output
# 定义标签到颜色的映射，例如：'leakage' 对应 (255, 0, 0) 表示红色
label_to_color = {
    'heart': (128, 0, 0),
    # 在这里添加更多标签和颜色
}
 
# 定义输入JSON文件夹和输出PNG文件夹
input_folder = r'D:\0.Data\pineapple\pineapple\test\label\json'  # 将此路径替换为包含JSON文件的文件夹路径
output_folder = r'D:\0.Data\pineapple\pineapple\test\png'  # 将此路径替换为要保存PNG文件的文件夹路径
 
# 确保输出文件夹存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
 
# 循环处理输入文件夹中的每个JSON文件
for json_filename in os.listdir(input_folder):
    if json_filename.endswith('.json'):
        # 构建输入JSON文件的完整路径
        json_file_path = os.path.join(input_folder, json_filename)
 
        # 读取JSON文件内容
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
 
            # 获取图像尺寸和标注
            img_width = data['imageWidth']
            img_height = data['imageHeight']
            shapes = data['shapes']
 
            # 创建一个空白的PNG图像
            img = Image.new('RGB', (img_width, img_height), (0, 0, 0))
            draw = ImageDraw.Draw(img)
 
            # 在图像上绘制每个标注
            for shape in shapes:
                label = shape['label']
                points = shape['points']
                polygon = [(x, y) for x, y in points]
 
                # 使用颜色映射来确定填充颜色
                if label in label_to_color:
                    fill_color = label_to_color[label]
                    draw.polygon(polygon, fill=fill_color)
                else:
                    print(f"警告：未知标签 '{label}'，将使用默认颜色绘制。")
 
            # 构建输出PNG文件的完整路径
            output_filename = os.path.splitext(json_filename)[0] + '.png'
            output_path = os.path.join(output_folder, output_filename)
 
            # 保存PNG图像
            img.save(output_path, 'PNG')
            print(f'转换: {json_file_path} -> {output_path}')
 
print('转换完成！')