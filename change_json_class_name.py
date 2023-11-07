import json
import os
import argparse
from tqdm import tqdm

# 对标注的json数据把其中的错误标签改为指定的
def change_json_class_name(er_class, nowclass, json_dir, save_dir):
    if not os.path.isdir(save_dir): #判断所在目录下是否有该文件名的文件夹
        os.makedirs(save_dir) 
    json_paths = os.listdir(json_dir)
 
    for json_path in tqdm(json_paths):
        # for json_path in json_paths:
        path = os.path.join(json_dir, json_path)
        with open(path, 'r') as load_f:
            json_dict = json.load(load_f)
            for shape_dict in json_dict['shapes']:
                labels = shape_dict['label']
                    #if(label)
                if(labels == er_class):
                    shape_dict['label'] = nowclass
                    with open(path,'w', encoding='utf-8') as r:
                        #定义为写模式，名称定义为r
        
                        json.dump(json_dict,r, ensure_ascii=False, indent=4)
                    #将dict写入名称为r的文件中
        load_f.close()    
        r.close()

if __name__ == "__main__":
    """
    python json2txt_nomalize.py --json-dir my_datasets/color_rings/jsons --save-dir my_datasets/color_rings/txts --classes "cat,dogs"
    """
    parser = argparse.ArgumentParser(description='json convert to txt params')
    parser.add_argument('--json-dir', type=str,default='D:/0.Data/pineapple/lme', help='json path dir')
    parser.add_argument('--save-dir', type=str,default='D:/0.Data/pineapple/lme_1/' ,help='txt save dir')
    args = parser.parse_args()
    json_dir = args.json_dir
    save_dir = args.save_dir
    er_class = "weed" # 错误标签
    nowclass = "line" # 纠正标签
    change_json_class_name(er_class, nowclass, json_dir, save_dir)