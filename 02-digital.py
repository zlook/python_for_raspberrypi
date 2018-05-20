import RPi.GPIO as GPIO
import time


pin_list = [4, 17, 10, 9, 11, 14, 15, 18]  # 外接引脚
#           g,  f,  e, d,  c,  b,  a, dp   # 对应数码管的段位
data_list = [
    (1, 0, 0, 0, 0, 0, 0, 1),  # 0
    (1, 1, 1, 1, 0, 0, 1, 1),  # 1
    (0, 1, 0, 0, 1, 0, 0, 1),  # 2
    (0, 1, 1, 0, 0, 0, 0, 1),  # 3
    (0, 0, 1, 1, 0, 0, 1, 1),  # 4
    (0, 0, 1, 0, 0, 1, 0, 1),  # 5
    (0, 0, 0, 0, 0, 1, 0, 1),  # 6
    (1, 1, 1, 1, 0, 0, 0, 1),  # 7
    (0, 0, 0, 0, 0, 0, 0, 1),  # 8
    (0, 0, 1, 0, 0, 0, 0, 1),  # 9
    (0, 0, 0, 1, 0, 0, 0, 1),  # a
    (0, 0, 0, 0, 0, 1, 1, 1),  # b
    (1, 0, 0, 0, 1, 1, 0, 1),  # c
    (0, 1, 0, 0, 0, 0, 1, 1),  # d
    (0, 0, 0, 0, 1, 1, 0, 1),  # e
    (0, 0, 0, 1, 1, 1, 0, 1),  # f
]


def dataled(n):
    '''
    点亮一个共阳极数码管,静态扫描方式
    '''
    GPIO.setmode(GPIO.BCM)  # set pinmode
    GPIO.setwarnings(False)
    GPIO.setup(pin_list, GPIO.OUT)  # 设置多通道输出模式
    GPIO.output(pin_list, data_list[n])  # 将参数传至list提取数据
    time.sleep(2)  # 显示两秒
    GPIO.cleanup


if __name__ == '__main__':
    while True:  # 循环
        num = int(input('请输入想让数码管显示的数字:'))
        dataled(num)
