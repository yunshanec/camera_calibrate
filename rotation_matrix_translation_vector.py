# -*- coding: utf-8 -*-
# @Time : 2021/08/06 09:10
# @Author : yunshan
# @File : rotation_matrix_translation_vector.py
import numpy as np


def rotation_matrix(alpha=0, beta=0, gamma=0):
    """
    计算旋转矩阵
    :param alpha: 绕x旋转角度
    :param beta: 绕y旋转角度
    :param gamma: 绕z旋转角度
    :return: 旋转矩阵
    """
    alpha = alpha * np.pi / 180
    beta = beta * np.pi / 180
    gamma = gamma * np.pi / 180

    r_x = np.array(
        [
            [1, 0, 0],
            [0, np.cos(alpha), np.sin(alpha)],
            [0, -np.sin(alpha), np.cos(alpha)],
        ]
    )
    r_y = np.array(
        [[np.cos(beta), 0, -np.sin(beta)], [0, 1, 0], [np.sin(beta), 0, np.cos(beta)]]
    )
    r_z = np.array(
        [
            [np.cos(gamma), np.sin(gamma), 0],
            [-np.sin(gamma), np.cos(gamma), 0],
            [0, 0, 1],
        ]
    )

    rotation_matrix = r_x * r_y * r_z

    return rotation_matrix


a = rotation_matrix(alpha=30, beta=30, gamma=30)

print(a, "\n", a.T, "\n", a * np.transpose(a))
