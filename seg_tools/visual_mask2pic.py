import os
import cv2
import numpy as np

"""
将json标注的信息映射回原图，展示标注信息,存放在masks文件夹下，得到jpg文件
"""
# 获取mask对应原始图片位置
def add_mask2image_binary(images_path, masks_path, masked_path):
    # Add binary masks to images
    for img_item in os.listdir(images_path):
        print(img_item)
        img_path = os.path.join(images_path, img_item)
        img = cv2.imread(img_path)
        mask_path = os.path.join(masks_path, img_item[:-4] + '.png')  # mask是.png格式的，image是.jpg格式的
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)  # 将彩色mask以二值图像形式读取
        masked = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint8), mask=mask)  # 将image的相素值和mask像素值相加得到结果
        cv2.imwrite(os.path.join(masked_path, img_item), masked)


# 注意使用全局路径，且无中文
images_path = r'image/images'
masks_path = r'image/json'
masked_path = r'image/masks'
add_mask2image_binary(images_path, masks_path, masked_path)
