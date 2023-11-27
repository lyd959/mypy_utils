# *_*coding: utf-8 *_*
# author --liming--
 
import os
import numpy as np
from osgeo import gdal
 #将tif文件分割为小文件，避免大文件无法操作,根据行划，列为全列

# 定义读取和保存图像的类
class GRID:
 
    def load_image(self, filename):
        image = gdal.Open(filename)

        #列数
        img_width = image.RasterXSize
        #行数
        img_height = image.RasterYSize
 
        img_geotrans = image.GetGeoTransform()
        img_proj = image.GetProjection()
        img_data = image.ReadAsArray(0, 0, img_width, img_height)
 
        del image
        print('行数： {},列数： {}'.format(img_height, img_width))
        return img_proj, img_geotrans, img_data
 
    def write_image(self, filename, img_proj, img_geotrans, img_data):
        # 判断栅格数据类型
        if 'int8' in img_data.dtype.name:
            datatype = gdal.GDT_Byte
        elif 'int16' in img_data.dtype.name:
            datatype = gdal.GDT_UInt16
        else:
            datatype = gdal.GDT_Float32
 
        # 判断数组维度
        if len(img_data.shape) == 3:
            img_bands, img_height, img_width = img_data.shape
        else:
            img_bands, (img_height, img_width) = 1, img_data.shape
 
        # 创建文件
        driver = gdal.GetDriverByName('GTiff')
        image = driver.Create(filename, img_width, img_height, img_bands, datatype)
 
        image.SetGeoTransform(img_geotrans)
        image.SetProjection(img_proj)
 
        if img_bands == 1:
            image.GetRasterBand(1).WriteArray(img_data)
        else:
            for i in range(img_bands):
                image.GetRasterBand(i+1).WriteArray(img_data[i])
 
        del image # 删除变量,保留数据
 
if __name__ == '__main__':
    import time
    import argparse
 
    parser = argparse.ArgumentParser(description='load remote sensing image and split to patch')
    parser.add_argument('--task_path',
                    default='C:/lyd_software/0.pythonCode/lyd_utils/task',
                    help='root dir')
    parser.add_argument('--patch_size',
                        default=1000,
                        help='patch size')
    parser.add_argument('--image',
                        default="C:/lyd_software/0.pythonCode/lyd_utils/task/image",
                        help='remote sensing image path')
    """
    parser.add_argument('--patch_save',
                        default='C://Users//V//Documents//DJI//DJITerra//wcl1991@qq.com//save//',
                        help='save path of patch image')
    """
    args = parser.parse_args()
    
    task_path = args.task_path
    if not os.path.exists(task_path): #判断是否存在文件夹如果不存在则创建为文件夹
        raise Exception("No task dir")
    image_path = args.image
    patch_save = task_path+"/patch_save"
    dictionary = task_path+"/dictionary"
    result_path = task_path+"/result"
    if not os.path.exists(patch_save):
        patch_save = os.makedirs(patch_save)
    if not os.path.exists(dictionary):
        os.makedirs(dictionary)
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    print('待处理图像路径为:{}'.format(args.image))
    print('行大小为:{}'.format(args.patch_size))
    print('分块图像保存路径:{}'.format(patch_save))

    image_list = os.listdir(image_path)
    #image_list.sort(key=lambda x:int(x[:-4])) 
    t_start = time.time()
    
    for k in range(len(image_list)):
        time_start = time.time()
        img_name = image_path +'//'+ image_list[k]
        proj, geotrans, data = GRID().load_image(img_name)

        # 图像分块
        patch_size = args.patch_size
        #patch_save = args.patch_save
        # 通道数，行数，列数
        channel, height, width = data.shape
        # 判断是否能完全划分
        if(height%patch_size == 0 ):
            numLine = height//patch_size
        else:
            numLine = height//patch_size+1

        num = 0
        for i in range(numLine):
        #for j in range(height//patch_size):
            sub_image = data[:, i*patch_size:(i+1)*patch_size, :]
            GRID().write_image(patch_save +"//"+ '{}.tif'.format(num), proj, geotrans, sub_image)
            num += 1

        time_end = time.time()
        print('第{}张图像分块完毕, 耗时:{}秒'.format(k+1, round((time_end-time_start), 4)))

    t_end = time.time()
    print('所有图像处理完毕,耗时:{}秒'.format(round((t_end-t_start), 4)))