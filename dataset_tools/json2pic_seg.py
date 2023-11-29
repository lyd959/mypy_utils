import os
import cv2
import numpy as np
import json


'''
制作一个只包含分类标注的标签图像，假如我们分类的标签为cat和dog，那么该标签图像中，Background为0，cat为1，dog为2。
我们首先要创建一个和原图大小一致的空白图像，该图像所有像素都是0，这表示在该图像中所有的内容都是Background。
然后根据标签对应的区域使用与之对应的类别索引来填充该图像，也就是说，将cat对应的区域用1填充，dog对应的区域用2填充。
特别注意的是，一定要有Background这一项且一定要放在index为0的位置。
'''
image_path = 'image/images'
masks_path = 'image/masks'
json_path = 'image/json'

if not os.path.exists(masks_path):
        os.makedirs(masks_path)
# 分类标签，一定要包含'Background'且必须放在最前面
category_types = ['background', 'line']
# 将图片标注json文件批量生成训练所需的标签图像png
imgpath_list = os.listdir(image_path)
for img_path in imgpath_list:
    img_name = img_path.split('.')[0]
    img = cv2.imread(os.path.join(image_path, img_path))
    h, w = img.shape[:2]
    # 创建一个大小和原图相同的空白图像
    mask = np.zeros([h, w, 1], np.uint8)

    with open(json_path+'/'+img_name+'.json', encoding='utf-8') as f:
        label = json.load(f)

    shapes = label['shapes']
    for shape in shapes:
        category = shape['label']
        points = shape['points']
        # 将图像标记填充至空白图像
        points_array = np.array(points, dtype=np.int32)
        mask = cv2.fillPoly(mask, [points_array], category_types.index(category))

    # 生成的标注图像必须为png格式
    cv2.imwrite(masks_path+'/'+img_name+'.png', mask)
