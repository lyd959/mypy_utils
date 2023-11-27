
import csv
import pandas as pd
import argparse


def savelonlat2csv(filedir):
    # 1. 创建小车执行文件
    f = open(filedir+'/result/task.csv','w',encoding='utf-8', newline='')
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    # 3. 构建列表头
    csv_writer.writerow(["lot","lat"])

    with open(filedir+"/result/line.csv", newline='') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件

        for line in csv_reader:            # 将csv 文件中的数据保存到data中
            # [列；行]
            rowline = line[0].split(" ")
            row = int(rowline[1])
            col = int(rowline[0])
            if(rowline[1]=='0'):
                break
            else:	
                print(str(rowline[0]),str(rowline[1]))
                if(row<1000):
                    file = 0
                else:
                    file = (row//1000) # 获取文件位置
                row = row%1000 # 获取行号
                col = col    # 获取列号
                csvPD=pd.read_csv(filedir+'/dictionary/'+str(file)+'.csv')
                print('------------搜寻------------')
                print(csvPD[str(col)][row][1:-1].split(','))
                # 经度
                lot = csvPD[str(col)][row][1:-1].split(',')[1]
                # 纬度
                lat = csvPD[str(col)][row][1:-1].split(',')[0]
                print(lot, lat)
                csv_writer.writerow([lot,lat])
                print('------------Done------------')
    # 5. 关闭文件
    f.close()
    print("任务文件已生成")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Trans latlot')
    parser.add_argument('--task_path',
                    default='C:/lyd_software/0.pythonCode/lyd_utils/task',
                    help='root dir')
    args = parser.parse_args()
    filedir = args.task_path
    savelonlat2csv(filedir)