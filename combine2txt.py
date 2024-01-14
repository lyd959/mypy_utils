import os
import glob

# 指定两个文件夹路径
folder1_path = r"D:\0.Data\pineapple\pineapple\multi_line_weed_dataset\plant_line\labels\val2017"
folder2_path = r"D:\0.Data\pineapple\pineapple\multi_line_weed_dataset\lane_line\labels\val2017"

# 输出文件夹路径
output_folder_path = r"C:/Users/V\Desktop/test2"

def merge_and_save_txt_files(folder1_path, folder2_path, output_folder_path):
    # 确保输出文件夹存在，如果不存在则创建
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # 获取两个文件夹下所有txt文件
    txt_files_folder1 = glob.glob(os.path.join(folder1_path, '*.txt'))
    txt_files_folder2 = glob.glob(os.path.join(folder2_path, '*.txt'))

    # 合并两个文件夹的txt文件并保存到新文件夹
    for txt_file_path1 in txt_files_folder1:
        # 获取同名文件在第二个文件夹中的路径
        txt_file_path2 = os.path.join(folder2_path, os.path.basename(txt_file_path1))

        # 如果同名文件存在，则合并内容并保存到新文件夹
        if os.path.exists(txt_file_path2):
            with open(txt_file_path1, 'r') as input_file1, open(txt_file_path2, 'r') as input_file2:
                # 读取文件内容
                content1 = input_file1.read()
                content2 = input_file2.read()

                # 合并内容
                merged_content = content1 + content2

                # 写入到新文件中
                output_file_path = os.path.join(output_folder_path, os.path.basename(txt_file_path1))
                with open(output_file_path, 'w') as output_file:
                    output_file.write(merged_content)

if __name__ == "__main__":
    merge_and_save_txt_files(folder1_path, folder2_path, output_folder_path)
