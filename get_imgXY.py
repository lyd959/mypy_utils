import cv2
import numpy as np
import math
import pandas as pd
import argparse

global img
global point1, point2, order, lists

# 标记点顺序值
order = 0
lists = np.zeros((100, 2), np.int32)
# Global variables
start_row, start_col = 0, 0
window_size = 500  # Adjust this based on your preference

# Function to update the displayed portion of the image
def update_display():
    global start_row, start_col, img

    displayed_image = img[start_row:start_row + window_size, start_col:start_col + window_size, :]
    cv2.imshow('image', displayed_image)

# Callback function for the horizontal scrollbar
def update_horizontal_position(pos):
    global start_col
    start_col = pos
    update_display()

# Callback function for the vertical scrollbar
def update_vertical_position(pos):
    global start_row
    start_row = pos
    update_display()
# 响应事件
def draw_circle(event, x, y, flags, param):
    global img,  point1, point2, order, lists
    img2 = img.copy()

    if event == cv2.EVENT_LBUTTONDOWN:   #左键点击
        point1 = (x,y)
        cv2.circle(img2, point1, 100, (0,255,0), 50)
        cv2.putText(img, f'* {order}', point1, cv2.FONT_HERSHEY_PLAIN,
                    10.0, (0,0,255), thickness = 25)
        # 列；行
        print(x,y)
        lists[order][0]=x
        lists[order][1]=y
        cv2.imshow('image', img2)

    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  #按住左键拖曳
        cv2.line(img2, point1, (x,y), (255,0,0), 50)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:    #左键释放
        point2 = (x,y)
        order = order+1
        cv2.line(img2, point1, point2, (0,0,255), 50)
        cv2.circle(img2, point2, 100, (0,255,0), 50)
        #cv2.putText(img, f'({x}, {y})', point2, cv2.FONT_HERSHEY_PLAIN,
         #   10.0, (0,0,255), thickness = 10)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_RBUTTONDOWN:    #右键点击
        print("finish line")
        """
        # points = np.array([[25,25], [50, 25], [25, 75], [150, 175], [5555, 4385]], np.int32)
        np.delete(lists, (order, -1), axis=1)
        lists = lists.reshape((-1, 1, 2))
        #points = points.reshape((-1, 1, 2))
        cv2.polylines(img2, [lists], True, (0,0,255), 50)
        """
        #cv2.imshow('image', img2)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_RBUTTONUP:    #右键释放
        # 根据标定顺序点生成航道线
        for i in range(0, order-1):
            cv2.line(img2, [lists[i][0], lists[i][1]], [lists[i+1][0], lists[i+1][1]], (0, 255, 0), 50)
        cv2.imshow('image', img2)

def savecsv(filedir):
    np.savetxt(filedir+"/result/line.csv", lists, fmt='%d')
    print('------------csv save done------------')


if __name__ == '__main__':     
    parser = argparse.ArgumentParser(description='Trans latlot')
    parser.add_argument('--task_path',
                    default='C:/lyd_software/0.pythonCode/lyd_utils/task',
                    help='root dir')
    args = parser.parse_args()
    filedir = args.task_path
    img=cv2.imread(filedir+'/image/result.tif')
    # 窗口设置
    cv2.namedWindow("image", 0)
    cv2.moveWindow("image", 100, 50)
    # 参数：宽, 高
    cv2.resizeWindow("image", 1200, 1000)
    cv2.createTrackbar('Horizontal', 'image', 0, img.shape[1] - window_size, update_horizontal_position)
    cv2.createTrackbar('Vertical', 'image', 0, img.shape[0] - window_size, update_vertical_position)

    # Display the initial portion of the image
    update_display()
    cv2.setMouseCallback("image", draw_circle)
    while(1):
        cv2.imshow("image", img)
        if cv2.waitKey(0)&0xFF==27:
            break
        elif cv2.waitKey(0) == ord('q'):
            if(order>0):
                order = order-1
        elif cv2.waitKey(0) == ord('s'):
            savecsv(filedir)
    cv2.destroyAllWindows()
