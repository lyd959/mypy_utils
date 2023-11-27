from osgeo import gdal
from pylab import *  # 支持中文
import pandas as pd
import csv
import os

if __name__ == "__main__":
    filePath = "C://lyd_software//0.pythonCode//lyd_utils//task"  # 文件路径
    #df = pd.read_csv(filePath)


    csv = filePath+'//csv'

    if not csv:
        os.makedirs(csv)