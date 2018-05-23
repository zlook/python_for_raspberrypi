#!/usr/bin/python3
import pygame
import socket
import sys


class ClientSocketCar(object):
    '''
    实例客户端套接字,用于发送数据
    '''
    def __init__(self):
        '''
        初始化套接字
        '''
        self.clinet_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
        self.clinet_socket.connect(('192.168.155.51', 9900))  # ip地址 ,端口号192.168.199.230

    # 发送数据
    def up_socket(self):
        self.clinet_socket.send('up'.encode('utf-8'))

    def down_socket(self):
        self.clinet_socket.send('down'.encode('utf-8'))

    def left_socket(self):
        self.clinet_socket.send('left'.encode('utf-8'))

    def right_socket(self):
        self.clinet_socket.send('right'.encode('utf-8'))

    def __del__(self):
        self.clinet_socket.close()


class Point(object):
    '''
    创建按钮类
    '''
    # 初始化
    def __init__(self):
        # 实例化socket对象
        self.car_socket = ClientSocketCar()
        # 载入图片
        self.image_point1 = pygame.image.load('point_vert.png')  # 图片1
        self.image_point2 = pygame.image.load('point_horiz.png')  # 图片2
        # 将图片对象转化成矩形对象
        self.img_rect1 = self.image_point1.get_rect()  # 矩形1 centerx=100, centery=130
        self.img_rect2 = self.image_point2.get_rect()  # 矩形2 centerx=390, centery=130
        self.img_rect1.move_ip(100, 130)
        self.img_rect2.move_ip(390, 130)
        # 按钮步进速度
        self.speed = 8

    def move_left(self):
        '''
        按钮向左移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的x方向位置
        if self.img_rect2[0] > 295:
            self.img_rect2.move_ip(-self.speed, 0)
            self.car_socket.left_socket()

    def move_right(self):
        '''
        按钮向右移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的x方向位置
        if self.img_rect2[0] < 485:
            # 改变按钮位置
            self.img_rect2.move_ip(self.speed, 0)
            # 发送数据
            self.car_socket.right_socket()

    def move_up(self):
        '''
        按钮向上移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的y方向位置
        if self.img_rect1[1] > 44:
            self.img_rect1.move_ip(0, -self.speed)
            self.car_socket.up_socket()

    def move_down(self):
        '''
        按钮向下移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的y方向位置
        if self.img_rect1[1] < 235:
            self.img_rect1.move_ip(0, self.speed)
            self.car_socket.down_socket()


class Windows(object):
    '''
    创建主窗口类
    '''
    # 初始化
    def __init__(self):
        # pygame 硬件初始化
        pygame.init()
        self.window = pygame.display.set_mode([640, 320])
        # 初始化界面及背景
        pygame.display.set_caption('小车控制')
        self.image = pygame.image.load('car.png')
        # 实例化按钮
        self.point_img = Point()

    def draw(self):
        '''
        将背景及按钮放入到主窗口
        '''
        self.window.blit(self.image, (0, 0))
        self.window.blit(self.point_img.image_point1, (self.point_img.img_rect1[0], self.point_img.img_rect1[1]))
        self.window.blit(self.point_img.image_point2, (self.point_img.img_rect2[0], self.point_img.img_rect2[1]))

    def event(self):
        '''
        检测并对事件进行响应
        '''
        # 获取当前事件类型,进行遍历
        self.event_list = pygame.event.get()
        for event in self.event_list:
            if event.type == pygame.QUIT:
                self.game_over()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.point_img.move_up()
                    print('加速加速--')
                if event.key == pygame.K_DOWN:
                    self.point_img.move_down()
                    print('减速减速--')
                if event.key == pygame.K_LEFT:
                    self.point_img.move_left()
                    print('左拐左拐--')
                if event.key == pygame.K_RIGHT:
                    self.point_img.move_right()
                    print('右拐右拐--')

    def update(self):
        '''
        更新画面信息显示
        '''
        pygame.display.update()

    def game_over(self):
        '''
        系统退出
        '''
        pygame.quit()
        sys.exit()

    def run(self):
        '''
        程序运行入口
        '''
        while True:
            self.draw()
            self.event()
            self.update()


if __name__ == '__main__':
    kong = Windows()
    kong.run()
