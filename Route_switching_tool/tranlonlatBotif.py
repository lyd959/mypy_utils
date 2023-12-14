
import csv
import os
import pandas as pd
import argparse
from osgeo import gdal
from osgeo import osr

#读取tif数据集
def readTif(fileName):
    dataset = gdal.Open(fileName)
    if dataset == None:
        print(fileName+"文件无法打开")
    return dataset
#获取仿射矩阵信息
def Getgeotrans(fileName):
    dataset = readTif(fileName)
    return dataset.GetGeoTransform()
#像素坐标转地理坐标
def pixel2Coord(Xpixel,Ypixel,GeoTransform):
    XGeo = GeoTransform[0]+GeoTransform[1]*Xpixel+Ypixel*GeoTransform[2]
    YGeo = GeoTransform[3]+GeoTransform[4]*Xpixel+Ypixel*GeoTransform[5]
    return XGeo,YGeo

def savelonlat2csv(filedir, dataset):
    # 1. 创建小车执行文件
    f = open(filedir+'/result/task.csv','w',encoding='utf-8', newline='')
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    # 3. 构建列表头
    csv_writer.writerow(["lot","lat"])


    with open(filedir+"/result/line.csv", newline='') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件

        for line in csv_reader:            # 将csv 文件中的数据保存到data中
            # line[列；行]
            rowline = line[0].split(" ")
            row = int(rowline[0])
            col = int(rowline[1])
            if(rowline[1]=='0'):
                break
            else:	
                XGeo, YGeo = pixel2Coord(row, col, dataset)
                print(XGeo, YGeo)

    # 5. 关闭文件
    f.close()
    print("任务文件已生成")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Trans latlot')
    parser.add_argument('--task_path',
                    default=r'C:\lyd_software\0.pythonCode\lyd_utils\Route_switching_tool\lanj2',
                    help='root dir')
    args = parser.parse_args()
    filedir = args.task_path
    img_name = filedir +'/image/result.tif'
    dataset = Getgeotrans(img_name)
    savelonlat2csv(filedir, dataset)