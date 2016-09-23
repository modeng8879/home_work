import socket

client = socket.socket()

client.connect(("localhost",8080))
while True:
    cmd = input(">>>: ").strip()
    if not cmd:
        continue
    client.send(cmd.encode('utf-8'))
    cmd_res_size =  client.recv(1024)
    print('命令结果大小: ',cmd_res_size,type(cmd_res_size))
    client.send(b'ack')
    received_size = 0
    received_data = b''
    while received_size != int(cmd_res_size):
        data = client.recv(1024)
        received_size += len(data)
        received_data += data

    else:
        print("cmd res receive done ...",received_size)
        print(received_data.decode())
client.close()

