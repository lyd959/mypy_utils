from PIL import Image, ImageDraw
import os

def txt_to_png(txt_filename, image_folder, output_folder):
    with open(txt_filename, 'r') as txt_file:
        lines = txt_file.readlines()

    for line in lines:
        # 假设每行的格式是 "class_name x_min y_min x_max y_max"
        parts = line.strip().split()
        class_name, x_min, y_min, x_max, y_max = parts

        # 构建图像路径
        image_filename = os.path.splitext(os.path.basename(txt_filename))[0] + '.png'
        image_path = os.path.join(image_folder, image_filename)

        # 读取图像
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        # 绘制目标分割框
        draw.rectangle([int(x_min), int(y_min), int(x_max), int(y_max)], outline='red', width=2)

        # 保存为 PNG 图像
        output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(txt_filename))[0] + '_segmentation.png')
        image.save(output_path, 'PNG')

# 指定你的 txt 文件夹、图像文件夹和输出 PNG 存储文件夹
txt_folder_path = 'D:/0.Data/pineapple/pineapple/test/label'
image_folder_path = 'D:/0.Data/pineapple/pineapple/test/image'
output_folder_path = 'D:/0.Data/pineapple/pineapple/test/png'

# 遍历并转换每个 txt 文件
for txt_filename in os.listdir(txt_folder_path):
    if txt_filename.endswith('.txt'):
        txt_path = os.path.join(txt_folder_path, txt_filename)
        txt_to_png(txt_path, image_folder_path, output_folder_path)
