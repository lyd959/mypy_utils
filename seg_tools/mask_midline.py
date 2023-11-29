import cv2
import numpy as np

# 根据分割结果适配外接矩阵，并为外接矩阵划中线
# flag:0代表在mask图上展示分割线，1代表在原始图上展示
flag = 0
# 读取图像
image = cv2.imread('image/val_batch0_pred.jpg')
origin_image = cv2.imread('image/val_batch0_pred.jpg')
# 窗口设置
cv2.namedWindow("image", 0)
cv2.moveWindow("image", 100, 50)
# 参数：宽, 高
cv2.resizeWindow("image", 1200, 1000)

# 将图像转换为灰度
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用阈值化将图像二值化，使非黑色部分为白色
_, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

# 寻找轮廓
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours = [contour for contour in contours if cv2.contourArea(contour) > 500]
print("Number of contours:", len(contours))

for contour in contours:

    # 获取当前轮廓的最小外接矩形
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    # 获取旋转角度和中心点坐标
    angle = rect[2]
    center = rect[0]

    # 计算旋转矩阵
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)

    # 获取矩形的四个角点坐标
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    # 输出四个角点坐标
    #print("Box Corners:", box)
    if(flag == 1):
        # 用矩形框住非黑色部分
        cv2.drawContours(origin_image, [box], 0, (0, 255, 0), 2)


        # 计算矩形的中线坐标
        mid_point1 = ((box[0][0] + box[3][0]) // 2, (box[0][1] + box[3][1]) // 2)
        mid_point2 = ((box[1][0] + box[2][0]) // 2, (box[1][1] + box[2][1]) // 2)

        # 画出矩形的中线
        cv2.line(origin_image, tuple(map(int, mid_point1)), tuple(map(int, mid_point2)), (0, 0, 255), 7)
    if(flag == 0):
        # 用矩形框住非黑色部分
        cv2.drawContours(image, [box], 0, (0, 255, 0), 2)


        # 计算矩形的中线坐标
        mid_point1 = ((box[0][0] + box[3][0]) // 2, (box[0][1] + box[3][1]) // 2)
        mid_point2 = ((box[1][0] + box[2][0]) // 2, (box[1][1] + box[2][1]) // 2)

        # 画出矩形的中线
        cv2.line(image, tuple(map(int, mid_point1)), tuple(map(int, mid_point2)), (0, 0, 255), 7)
    print("像素点为：[{}，{}]".format(mid_point1, mid_point2))
 
# 显示结果
if(flag == 0):
    cv2.imshow('image', image)
if(flag == 1):
    cv2.imshow('image', origin_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
