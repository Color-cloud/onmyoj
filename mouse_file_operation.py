import win32api
import numpy as np
import win32con
from ctypes import windll
import time
import win32gui
import os

last_class = ''


# 鼠标点击指定坐标 down是按下 up是松开
def click_single(shubiao_x, shubiao_y, my_class):
    global last_class

    # if my_class == 'tz' and last_class == 'tz':
    #     return
    for i in range(1):
        windll.user32.SetCursorPos(int(shubiao_x), int(shubiao_y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 1320, 1)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 1320, 1)
    last_class = my_class


def delete_img(path):
    image_list = os.listdir(path)

    if len(image_list) > 30:
        os.remove('%s/%s' % (path, image_list[0]))
