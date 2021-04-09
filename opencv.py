import time
from ctypes import windll
from fnmatch import fnmatch

import win32api
import numpy as np
import win32con
import cv2
import win32gui
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtGui import *
import win32gui
import sys
import re
import math
import pytesseract

# 获取当前屏幕的尺寸 即分辨率
width = windll.user32.GetSystemMetrics(0)
height = windll.user32.GetSystemMetrics(1)
# print(width, height)

#
# # 鼠标点击指定坐标 down是按下 up是松开
# for i in range(2):
#     windll.user32.SetCursorPos(1320, 1)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 1320, 1)
#     time.sleep(0.05)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 1320, 1)
######################################
hwnd_title = dict()


# 显示所有窗口的hwnd以及title
def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        # print(win32gui.GetWindowText(hwnd))
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


# 得到所有当前打开的程序的hwnd和title
win32gui.EnumWindows(get_all_hwnd, 0)


def show_all_hwdn():
    for h, t in hwnd_title.items():
        if t is not "":
            print(h, t)


# ############################################
# # 截全屏
# # hwnd = win32gui.FindWindow(None, 'C:/Windows/system32/cmd.exe')
# # 截某个程序的屏
# hwnd = win32gui.FindWindow(None, hwnd_title[1901680])
# app = QApplication(sys.argv)
# screen = QApplication.primaryScreen()
# img = screen.grabWindow(hwnd).toImage()
# img.save("screenshot.jpg")
def return_want(app_name):
    hs = []
    for h, t in hwnd_title.items():
        if fnmatch(t, '*%s*' % app_name):
            hs.append(h)
    return hs


# 截取传入参数（hwnd）程序的图 存储截图并返回图像名称
def print_app_screen(hwnd_number):
    no_name = ['.', ':', '/', '\\', '：', '?', '？', '=']
    try:
        hwnd = int(hwnd_number)
        # hwnd = win32gui.FindWindow(None, hwnd_title[hwnd_number])
        app = QApplication(sys.argv)
        screen = QApplication.primaryScreen()
        _, _, x_hwnd, y_hwnd = win32gui.GetWindowRect(hwnd)
        img = screen.grabWindow(hwnd).toImage()
        img_index = re.search('-', hwnd_title[hwnd_number][::-1]).span()[0]
        img_name = hwnd_title[hwnd_number][int(-img_index):]
        timestring1 = str(time.time())
        timestring = timestring1[2:10] + timestring1[11:13]
        for i in img_name:
            if i in no_name:
                img_name = img_name.replace(i, '')
        img.save("./images/%s_%s.jpg" % (img_name, timestring))
        # print("生成 %s_%s.jpg" % (img_name, timestring))
        return "%s_%s.jpg" % (img_name, timestring), [x_hwnd, y_hwnd]
    except KeyError:
        return None

    # except:
    #     hwnd = win32gui.FindWindow(None, hwnd_number)
    #     app = QApplication(sys.argv)
    #     screen = QApplication.primaryScreen()
    #     img = screen.grabWindow(hwnd).toImage()
    #     timestring = int(time.time())
    #     img.save("./images/%s_%s.jpg" % ('screen', timestring))
    #     print("生成%s_%s.jpg" % ('screen', timestring))
    #     return "%s_%s.jpg" % ('screen', timestring)


# 读取图像，解决cv2.imread不能读取中文路径的问题
def cv_imread(filePath):
    cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
    # imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    # cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
    return cv_img


# 创建一个窗口
def show_img(img_read):
    cv2.namedWindow("Imagess")
    # 然后在窗口中显示图像
    cv2.imshow("Imagess", img_read)
    # 如果不添waitkey这一句，在IDLE中执行窗口直接无响应。在命令行中执行的话，则是一闪而过。
    # waitkey是一个键盘绑定函数。需要指出的是它的时间尺度是毫秒级。函数等待特定的几毫秒，看是否有键盘输入。
    # 特定的几毫秒之内，如果 按下任意键，这个函数会返回按键的 ASCII码值，程序将会继续运行。
    # 如果没有键盘输入，返回值为 -1，如果我们设置这个函数的参数为 0，那它将会无限期的等待键盘输入。它也可以被用来检测特定键是否被按下。
    cv2.waitKey(0)
    # 释放窗口
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_all_hwdn()
    # input_image = print_app_screen(1443216)

    # img = cv_imread("./images/%s" % input_image[0])
    # img = cv_imread("./%s" % 'eee.jpg')
    # show_img(img)
# tesseract OCR 识别
# text = pytesseract.image_to_string(img, lang='chi_sim')
# print(text)
