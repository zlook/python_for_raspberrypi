import socket


def client_socket(ip, num):
    led_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建服务器套接字
    led_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 关闭程序时立即释放端口
    led_client.connect((ip, 9999))
    print('链接成功!')
    led_client.send(num.encode('utf-8'))
    print('发送成功!')
    led_client.close()


if __name__ == '__main__':
    ip_data = input('请输入服务器IP:')
    num_data = input('请输入显示的数字:')
    client_socket(ip_data, num_data)
