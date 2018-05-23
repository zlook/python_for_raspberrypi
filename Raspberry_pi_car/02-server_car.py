#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import socket


class ServerSocketCar(object):
    '''
    创建服务端通信socket
    '''
    def __init__(self):

        # 实例化CarPi对象
        self.car_pi = CarPi()
        # 创建服务器socket并进行端口绑定监听
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('', 9900))
        self.server_socket.listen(128)

    def recv_socket(self):
        # 链接成功,返回客户端通信socket
        self.client_socket, self.port_ip = self.server_socket.accept()
        # 打印当前链接客户端
        print('链接成功,客户端是:', self.port_ip)
        # 接收发送内容
        while True:
            # 接收数据,并解码
            self.date = self.client_socket.recv(1024)
            self.recv_data = self.date.decode('utf-8')
            # 当数据为空时,表示断开链接,结束,继续监听下一个客户端
            if not self.recv_data:
                print('链接断开--bye')
                # 占空比设置为50%
                self.car_pi.dc = 50
                return
            # 调用CarPi实例化方法,进行硬件部分操作
            self.car_pi.car_way(self.recv_data)

    def main_run(self):
        '''
        程序运行入口
        '''
        while True:
            self.recv_socket()

    def __del__(self):
        '''
        实例结束时资源回收
        '''
        self.client_socket.close()
        self.server_socket.close()


class CarPi(object):
    '''
    创建Raspberry类
    '''
    # 初始化硬件
    def __init__(self):
        # 初始化引脚
        GPIO.setmode(GPIO.BCM)  # set pinmode 设置管脚模式
        GPIO.setwarnings(False)  # 忽略引脚设置报错.引脚非in状态报错
        # # my GPIO [4, 17, 10 ,9, 11, 14, 15 ,18 ,23 ,24, 25, 8, 7]
        # # 两个软件pwm, 两个方向接口
        GPIO.setup((4, 17), GPIO.OUT)
        self.pin_p1 = GPIO.PWM(4, 50)
        self.pin_p2 = GPIO.PWM(17, 50)
        # 占空比
        self.dc = 50
        self.pin_p1.start(self.dc)
        self.pin_p2.start(self.dc)

    def car_way(self, way):
        '''
        小车运行状态,变更
        '''
        # print('开头--', self.dc)
        # 占空比必须为0~100否则自动结束
        if way == 'up' and 0 <= self.dc < 100:
            self.dc += 3
            self.pin_p1.ChangeDutyCycle(self.dc)
            self.pin_p2.ChangeDutyCycle(self.dc)
            # print('速度+1', self.dc)
        if way == 'down' and 0 < self.dc <= 100:
            self.dc -= 3
            self.pin_p1.ChangeDutyCycle(self.dc)
            self.pin_p2.ChangeDutyCycle(self.dc)
            # print('速度-1', self.dc)
        if way == 'left':
            GPIO.setup((10, 9), GPIO.OUT)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(9, GPIO.HIGH)
            GPIO.cleanup((10, 9))
            # print('左拐+1')
        if way == 'right':
            GPIO.setup((10, 9), GPIO.OUT)
            GPIO.output(10, GPIO.HIGH)
            GPIO.output(9, GPIO.LOW)
            GPIO.cleanup((10, 9))
            # print('右拐-1')

    def __del__(self):
        '''
        运行结束后,清理输出端口
        '''
        GPIO.cleanup()


if __name__ == '__main__':
    car = ServerSocketCar()
    car.main_run()
