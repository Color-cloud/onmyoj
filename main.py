# import cv2
import time
# import get_zuobiao
# import numpy as np
# import pytesseract
import opencv  # 同目录下自定义的py文件
import mouse_file_operation
from yolo import YOLO
from PIL import Image

# import keyboard

# from pynput.keyboard import Key
#
#########################################
path = './images'
app_name = '阴阳师'
#########################################


yolo = YOLO()
hwnds = opencv.return_want(app_name)

want_hwnd1 = hwnds[0]
want_hwnd2 = hwnds[1]
biaoshi = 0
tz_zuobiao = 0.75
jx_zuobiao = 2

while True:
    time.sleep(0.5)

    # input_image = opencv.print_app_screen('C:/Windows/system32/cmd.exe')
    input_image1 = opencv.print_app_screen(want_hwnd1)
    mouse_file_operation.delete_img(path)  # 删除images文件夹多余图像（每次删除文件夹第一张）
    input_image2 = opencv.print_app_screen(want_hwnd2)
    mouse_file_operation.delete_img(path)  # 删除images文件夹多余图像（每次删除文件夹第一张）
    try:
        img1 = "./images/%s" % input_image1[0]
        x_hwnd_1, y_hwnd_1 = input_image1[1]  # 程序相对于整个屏幕的右下角坐标
        image1 = Image.open(img1)
        img2 = "./images/%s" % input_image2[0]
        x_hwnd_2, y_hwnd_2 = input_image2[1]  # 程序相对于整个屏幕的右下角坐标
        image2 = Image.open(img2)
    except:
        print('Open Error! Try again!')
        continue
    if biaoshi == 20000:
        break
    else:
        r_image1 = yolo.detect_image(image1)
        print('检测img 1：', img1)
        r_image2 = yolo.detect_image(image2)
        print('检测img 2：', img2)
        # r_image[0].show()

    if type(r_image1) == tuple:
        print('img 1', r_image1[2])
        if 'tz' in r_image1[2].keys():
            if float(r_image1[2]['tz']) > 0.92:
                shubiao_x_1 = x_hwnd_1 - r_image1[1][0] * tz_zuobiao
                shubiao_y_1 = y_hwnd_1 - r_image1[1][1] * tz_zuobiao
                time.sleep(0.3)
                mouse_file_operation.click_single(shubiao_x_1, shubiao_y_1, 'tz')
                biaoshi += 1
                print('***************************************')
                print('当前为第%s轮' % biaoshi)
                print('***************************************')
        elif 'jx' in r_image1[2].keys():
            shubiao_x_1 = x_hwnd_1 - r_image1[1][0] * jx_zuobiao
            shubiao_y_1 = y_hwnd_1 - r_image1[1][1] * jx_zuobiao
            mouse_file_operation.click_single(shubiao_x_1, shubiao_y_1, 'jx')
    if type(r_image2) == tuple:
        print('img 2', r_image2[2])
        if 'tz' in r_image2[2].keys():
            if float(r_image2[2]['tz']) > 0.92:
                shubiao_x_2 = x_hwnd_2 - r_image2[1][0] * tz_zuobiao
                shubiao_y_2 = y_hwnd_2 - r_image2[1][1] * tz_zuobiao
                time.sleep(0.3)
                mouse_file_operation.click_single(shubiao_x_2, shubiao_y_2, 'tz')
                biaoshi += 1
                print('***************************************')
                print('当前为第%s轮' % biaoshi)
                print('***************************************')
        elif 'jx' in r_image2[2].keys():
            shubiao_x_2 = x_hwnd_2 - r_image2[1][0] * jx_zuobiao
            shubiao_y_2 = y_hwnd_2 - r_image2[1][1] * jx_zuobiao
            mouse_file_operation.click_single(shubiao_x_2, shubiao_y_2, 'jx')
