import os
import random
import shutil


'''
├── data(按照7:2:1比例划分)
│   ├── train 存放用于训练的图片
│   ├── trainannot 存放用于训练的图片标注
│   ├── val 存放用于验证的图片
│   ├── valannot 存放用于验证的图片标注
│   ├── test 存放用于测试的图片
│   ├── testannot 存放用于测试的图片标注
'''
# 数据集原始图片所存放的文件夹，必须为png文件
imagefilepath = 'D:/0.Data/pineapple/pineapple/pineapple_line_seg'

# 创建数据集文件夹
dirpath_list = [imagefilepath+'/dataset_seg/train', imagefilepath+'/dataset_seg/trainannot', 
                imagefilepath+'/dataset_seg/val', imagefilepath+'/dataset_seg/valannot', 
                imagefilepath+'/dataset_seg/test', imagefilepath+'/dataset_seg/testannot']
for dirpath in dirpath_list:
    if os.path.exists(dirpath):
        shutil.rmtree(dirpath)   # 删除原有的文件夹
        os.makedirs(dirpath)   # 创建文件夹
    elif not os.path.exists(dirpath):
        os.makedirs(dirpath)

# 训练集、验证集、测试集所占比例
train_percent = 0.8
val_percent = 0.1
test_percent = 0.1


total_img = os.listdir(imagefilepath+'/images')
# 所有数据集的图片名列表
total_name_list = [row.split('.')[0] for row in total_img]
num = len(total_name_list)
num_list = range(num)
# 训练集、验证集、测试集所包含的图片数目
train_tol = int(num * train_percent)
val_tol = int(num * val_percent)
test_tol = int(num * test_percent)

# 训练集在total_name_list中的index
train_numlist = random.sample(num_list, train_tol)
# 验证集在total_name_list中的index
val_test_numlist = list(set(num_list) - set(train_numlist))
val_numlist = random.sample(val_test_numlist, val_tol)
# 测试集在total_name_list中的index
test_numlist = list(set(val_test_numlist) - set(val_numlist))

# 将数据集和标签图片安装分类情况依次复制到对应的文件夹
for i in train_numlist:
    img_path = imagefilepath+'/images/'+total_name_list[i]+'.jpg'
    new_path = imagefilepath+'/dataset_seg/train/'+total_name_list[i]+'.jpg'
    shutil.copy(img_path, new_path)
    img_path = imagefilepath+'/masks/' + total_name_list[i] + '.png'
    new_path = imagefilepath+'/dataset_seg/trainannot/' + total_name_list[i] + '.png'
    shutil.copy(img_path, new_path)
for i in val_numlist:
    img_path = imagefilepath+'/images/'+total_name_list[i]+'.jpg'
    new_path = imagefilepath+'/dataset_seg/val/'+total_name_list[i]+'.jpg'
    shutil.copy(img_path, new_path)
    img_path = imagefilepath+'/masks/' + total_name_list[i] + '.png'
    new_path = imagefilepath+'/dataset_seg/valannot/' + total_name_list[i] + '.png'
    shutil.copy(img_path, new_path)
for i in test_numlist:
    img_path = imagefilepath+'/images/'+total_name_list[i]+'.jpg'
    new_path = imagefilepath+'/dataset_seg/test/'+total_name_list[i]+'.jpg'
    shutil.copy(img_path, new_path)
    img_path = imagefilepath+'/masks/' + total_name_list[i] + '.png'
    new_path = imagefilepath+'/dataset_seg/testannot/' + total_name_list[i] + '.png'
    shutil.copy(img_path, new_path)
