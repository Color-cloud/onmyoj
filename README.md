本打算直接通过控制鼠标的方式来做自动刷御魂或者觉醒的
但是由于不能每局刷的时间都精确到1e-2 所以最后用了图像识别来做

神经网络使用的Yolov4， 因本人电脑硬件问题 为节约训练时间 模型只训练了两个类别 分别是开始时的“挑战”和结束是的“点击屏幕继续”

使用方法：


1. 将jx_tz.pth 权重文件放在目录model_data下（该文件放在百度网盘了：链接：https://pan.baidu.com/s/1UDXb-xUMQhYQAjlkBk0J5g 提取码：1234 ）

2. 运行main.py文件即可（务必使用管理员权限运行）。

注意事项：
1. 因为原理是图像识别后控制鼠标进行点击 所以请将双开的阴阳师界面放在顶层。
2. 如果电脑没有独显或者显卡是AMD系列，请将yolo.py第28行“cuda = True”改为“cuda = False”