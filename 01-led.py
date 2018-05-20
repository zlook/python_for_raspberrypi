import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # set pinmode 设置管脚模式
GPIO.setwarnings(False)  # 忽略引脚设置报错.引脚非in状态报错


def led(n):
    '''
    点亮管脚
    my GPIO [4, 17, 10 ,9, 11, 14, 15 ,18 ,23 ,24, 25, 8, 7]
    num取值根据外部接线
    '''
    GPIO.setup(n, GPIO.OUT)  # | GPIO.IN or GPIO.OUT 设置输入或输入模式
    GPIO.output(n, GPIO.HIGH)
    time.sleep(3)  # 延时3秒
    GPIO.cleanup()  # 将引脚状态清空


if __name__ == '__main__':
    num = int(input('请输入外接引脚编号:'))  # 将输入转换成int
    led(num)
