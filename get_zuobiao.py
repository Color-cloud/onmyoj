import cv2


# src = cv2.imread("./eee.jpg")
# src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
# print("鼠标选择ROI,然后点击 enter键")
def select_kuang(src):
    # src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
    r = cv2.selectROI('input', src, False)  # ,返回 (x_min, y_min, w, h)
    # k = cv2.waitKey(0) & 0xFF
    # if k == 27:  # 按esc 键即可退出
    cv2.destroyWindow('input')
    print("ROI", r)
    return r


# roi区域
# roi = src[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

