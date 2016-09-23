import os
import socket

server = socket.socket()
server.bind(('localhost',8080))
server.listen()
print("等待客户端的链接。。。")
while True:
    conn,addr = server.accept()
    print("新链接",addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("已断开")
            break
        print("执行指令",data,type(data))
        cmd_res = os.popen(str(data, encoding = "utf-8")).read() #发挥结果为 unicode 编码的str 返回<class 'str'>
        print(cmd_res)
        cmd_res_bytes = bytes(cmd_res, encoding= 'utf-8')
        cmd_res_len_bytes = bytes(str(len(cmd_res_bytes)),encoding = 'utf-8')

        print(len(cmd_res),type(cmd_res)) #1726 <class 'str'>
        print('before cmd_res_bytes send',cmd_res_len_bytes)
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output ...."

        conn.send(cmd_res_len_bytes) #发送bytes
        ack = conn.recv(512)
        print(ack,type(ack))
        conn.send(cmd_res_bytes)
        print('send done')

server.close()
