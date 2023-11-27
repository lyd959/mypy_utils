import os
import re
"""
有些人想讲多个独立的数据集合并一起训练，此时往往遇到一个问题，比如有两类，这两类原来打标签时，类别序号均为0，现在就不能直接合并在一起，需要将某一类标签改为1，然后再合并，才不至于导致种类混乱（否则标签序号只有0，认为是一类，但配置的nc又是2）
先不合并标签，只对一个数据集标签文件夹下的所有txt进行修改。
"""

# 路径
path = r"D:/0.Data/pineapple/pineapple/multi_line_weed/seg_line/val2017/"
# 文件列表
files = []
for file in os.listdir(path):
    if file.endswith(".txt"):
        files.append(path+file)
# 逐文件读取-修改-重写
for file in files:
    with open(file, 'r') as f:
        new_data = re.sub('^0', '1', f.read(), flags=re.MULTILINE)    # 将列中的1替换为0
    with open(file, 'w') as f:
        f.write(new_data)
