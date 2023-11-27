import cv2

for shape in shapes:
    category = shape['label']
    points = shape['points']
    # 将图像标记填充至空白图像
    points_array = np.array(points, dtype=np.int32)
    # mask = cv2.fillPoly(mask, [points_array], category_types.index(category))

    if category == 'Gingerbread':
        # 调试时将某种标注的填充颜色改为255，便于查看用，实际时不需进行该操作
        mask = cv2.fillPoly(mask, [points_array], 125)
    elif category == 'Coconutmilk':
        mask = cv2.fillPoly(mask, [points_array], 255)
    else:
        mask = cv2.fillPoly(mask, [points_array], category_types.index(category))

cv2.imshow('mask', mask)
cv2.waitKey(0)
