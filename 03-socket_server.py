import RPi.GPIO as GPIO
import socket


def led_socket():
    '''
    socket网络接收程序
    '''
    led_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建服务器套接字
    led_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 关闭程序时立即释放端口
    led_server.bind(('', 9999))  # 释放ip绑定端口号9999
    led_server.listen(128)  # 监听端口
    led_cliect, ip_port = led_server.accept()  # 链接成功返回客户端套接字
    print('客户端IP端口', ip_port)  # 打印host/端口
    data = led_cliect.recv(1024)  # 接收信息
    data_int = data.decode('utf-8')
    date_led(int(data_int))
    print('显示成功!')
    led_cliect.close()
    led_server.close()


def date_led(a):
    '''
    led显示程序
    '''
    GPIO.setmode(GPIO.BCM)  # set pinmode
    GPIO.setwarnings(False)
    #  [4, 17, 10 ,9, 11, 14, 15 ,18 ,23 ,24, 25, 8, 7]
    #           g, f,   e, d,  c,  b,  a, dp
    led_list = [4, 17, 10, 9, 11, 14, 15, 18]
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
    # a = input('please input data')
    GPIO.setup(led_list, GPIO.OUT)
    GPIO.output(led_list, data_list[a])
    GPIO.cleanup


if __name__ == '__main__':
    led_socket()
