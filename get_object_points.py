# -*- coding: utf-8 -*-
# @Time : 2021/08/06 14:31
# @Author : yunshan
# @File : make_object_points.py
import numpy as np


def make_object_points(image_number,distance_mm = 2.5):
    x_list = []
    for x in range(0,7):
        x_list.append(x*distance_mm)

    y_list = x_list.copy()

    object_points = []
    for i in range(image_number):
        for x in x_list:
            for y in y_list:
                object_points.append([x,y,0.0])

    return np.array(object_points)

if __name__ == '__main__':
    object_positions = make_object_points(image_number=45,distance_mm = 2.5)
    np.savetxt("./result/object_points.out",object_positions)
    print('save object_points successful')

