# -*- coding: utf-8 -*-
# @Time : 2022/01/06 13:22
# @Author : yunshan
# @File : attitude_estimation.py
import cv2
import numpy as np

class AttitudeEstimation:
    def __init__(self,mtx,dist):
        self.mtx = mtx
        self.dist = dist

    def draw_line(self,img,corners,rvecs,tvecs) :
        axis = np.float32([[10, 0, 0], [0, 10, 0], [0, 0, -50]]).reshape(-1, 3)
        img_pts, _ = cv2.projectPoints(axis, rvecs, tvecs, self.mtx, self.dist)
        corner = tuple([int(x) for x in corners[0].ravel()])
        img = cv2.line(img, corner, tuple([int(x) for x in img_pts[0].ravel()]), (255, 0, 0), 5)
        img = cv2.line(img, corner, tuple([int(x) for x in img_pts[1].ravel()]), (0, 255, 0), 5)
        img = cv2.line(img, corner, tuple([int(x) for x in img_pts[2].ravel()]), (0, 0, 255), 5)

        return img

    def draw_rectangle(self,img,rvecs,tvecs):
        axis = np.float32([[0, 0, 0], [0, 5, 0], [5, 5, 0], [5, 0, 0], [0, 0, -5], [0, 5, -5], [5, 5, -5], [5, 0, -5]])
        img_pts, _ = cv2.projectPoints(axis, rvecs, tvecs, self.mtx, self.dist)
        imgpts = np.int32(img_pts).reshape(-1, 2)
        img = cv2.drawContours(img, [imgpts[:4]], -1, (0, 255, 0), -3)
        for i, j in zip(range(4), range(4, 8)) :
            img = cv2.line(img, tuple([int(x) for x in imgpts[i].ravel()]), tuple([int(x) for x in imgpts[j].ravel()]), (255), 3)
        img = cv2.drawContours(img, [imgpts[4 :]], -1, (0, 0, 255), 3)

        return img


if __name__ == '__main__':
    mtx = np.loadtxt('./result/right/right_mtx.out')
    dist = np.loadtxt("./result/right/right_dist.out")

    rvecs = np.loadtxt("./result/right/right_rvecs.out")
    tvecs = np.loadtxt("./result/right/right_tvecs.out")

    coor = AttitudeEstimation(mtx, dist)
    corners_pos = np.loadtxt("./result/right/image_points/right_points.out")
    all_corners_pos = corners_pos.reshape(45, 49, 2)

    for i in range(len(rvecs)):
        rvec = rvecs[i]
        tvec = tvecs[i]
        image = cv2.imread('./right_img/{}.png'.format(i))
        corners_pos = all_corners_pos[i]
        img = coor.draw_line(image,corners_pos,rvec,tvec)
        # img = coor.draw_rectangle(image,rvec,tvec)

        # cv2.imwrite("./result/right/attitude_estimation_line/{}.png".format(i),img)
        cv2.namedWindow("result_image", 0)
        cv2.resizeWindow("result_image", 1000, 1000)
        cv2.imshow("result_image", img)
        cv2.waitKey(50)
        cv2.destroyAllWindows()


