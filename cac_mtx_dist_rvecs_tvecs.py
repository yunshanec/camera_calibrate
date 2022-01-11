# -*- coding: utf-8 -*-
# @Time : 2021/08/09 13:43
# @Author : yunshan
# @File : cac_mtx_dist_rvecs_tvecs.py
import cv2
import numpy as np
from loguru import logger

def cac_mtx_dist_rvec_tvec(img_size,object_points,img_points):
    assert len(img_size) == 2,"chess board image: width, height"
    ret, mtx, dist, rotation_vecs, translations_vecs = cv2.calibrateCamera(object_points, img_points, img_size[::-1], None, None)
    logger.info(f"mtx 内参数矩阵:\n{mtx}\n")  # 内参数矩阵
    logger.info(f"dist 畸变系数:\n{dist}\n")
    logger.info(f"rvecs 旋转向量:\n{rotation_vecs}\n")  # 旋转向量  # 外参数
    logger.info(f"tvecs 平移向量:\n{translations_vecs}\n")  # 平移向量  # 外参数

    # 反向投影误差验证
    mean_error = 0
    for i in range(len(object_points)):
        img_points2, _ = cv2.projectPoints(object_points[i], rotation_vecs[i], translations_vecs[i], mtx, dist)
        error = cv2.norm(img_points[i], img_points2, cv2.NORM_L2) / len(img_points2)
        mean_error += error
    total_error = np.array([mean_error / len(object_points)])
    logger.warning(f"反向投影误差:{total_error}  越接近0越好")

    return ret, mtx, dist, rotation_vecs, translations_vecs,total_error

if __name__ == '__main__':
    object_points = np.loadtxt("./result/object_points.out").reshape(45, 49, 1, 3).astype(np.float32)
    left_image_points = np.loadtxt("./result/left/image_points/left_points.out").reshape(45, 49, 1, 2).astype(
        np.float32)
    img = cv2.imread("left_img/0.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_size = gray.shape
    ret,mtx,dist,rotation_vecs,translations_vecs,total_error = cac_mtx_dist_rvec_tvec(img_size=img_size,object_points=object_points,img_points=left_image_points)

