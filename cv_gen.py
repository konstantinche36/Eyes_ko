import cv2 as cv
from PIL import ImageGrab
import numpy as np
import teleg_msn
import time

START_X_POS, START_Y_POS, END_X_POS, END_Y_POS = 0, 0, 0, 0


def set_pos_coors(start_x_pos, start_y_pos, end_x_pos, end_y_pos):
    global START_X_POS, START_Y_POS, END_X_POS, END_Y_POS
    START_X_POS = start_x_pos
    START_Y_POS = start_y_pos
    END_X_POS = end_x_pos
    END_Y_POS = end_y_pos


def get_shoot():
    # screen_img = np.array(ImageGrab.grab(bbox=(start_x_pos, start_y_pos, end_x_pos, end_y_pos)))
    print((START_X_POS, START_Y_POS, END_X_POS, END_Y_POS))
    mat1 = np.array(ImageGrab.grab(bbox=(START_X_POS, START_Y_POS, END_X_POS, END_Y_POS)))
    return mat1
    # cv.imshow('screen', screen_img)
    # cv.waitKey()


def show_screen(mat):
    cv.imshow('screen', mat)
    cv.waitKey()


def get_cur_shoot(start_x_pos, start_y_pos, end_x_pos, end_y_pos):
    pass


def compare_imgs(mat1, mat2):
    return np.array_equal(mat1, mat2)


def compare_imgs_pos(mat1, mat2):
    return mat1[5:5] == mat2[5:5]


def foo(mat1):
    while True:
        if compare_imgs(mat1, get_shoot()):
            print('ok')

        else:
            print('not ok')
            teleg_msn.send_msn('Message in skype!!!')
            # break
        time.sleep(20)
# # print(mat1)
# while True:
#     if compare_imgs(mat1, get_shoot()):
#         print('ok')
#     else:
#         print('not ok')
