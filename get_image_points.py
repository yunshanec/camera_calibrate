# -*- coding: utf-8 -*-
# @Time : 2021/08/19 16:39
# @Author : yunshan
# @File : get_image_points.py
import cv2
import numpy as np
from sort_corners_box import Sort_corners_box

ori_point = Sort_corners_box(w=7, h=7)
with open("result/right/image_points/right_points.out", "ab") as f:
    for i in range(45):
        image_right = cv2.imread("./right_img/{}.png".format(i))
        result_right_image, corners_box_right = ori_point.run(image_right, flag=0)
        # print(corners_box_right)
        np.savetxt(f, np.array(corners_box_right))
        print("ok!!!!!!!!!!!!!")
