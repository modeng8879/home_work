import hashlib
import socket

client = socket.socket()

client.connect(("localhost",8080))
while True:
    cmd = input(">>>: ").strip()
    cmd = "get my_hash.py"
    print(cmd,type(cmd))
    if not cmd:
        continue

    if cmd.startswith("get"):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print("server response:" ,server_response)
        client.send(b"ready to recv file")
        file_total_size = int(server_response)
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename + ".new",'wb')
        m = hashlib.md5()
        while received_size < file_total_size:
            if file_total_size - received_size > 1024:
                size = 1024
            else:
                size = file_total_size - received_size
            data  = client.recv(size)
            received_size += len(data)
            m.update(data)
            f.write(data)
        else:
            new_file_md5 = m.hexdigest()
            print("file recv done", received_size,file_total_size)
            f.close()

        server_file_md5 = client.recv(1024)
        print("server file md5:", server_file_md5,)
        print("client file md5:", new_file_md5)
    # client.send(cmd.encode('utf-8'))
    # cmd_res_size =  client.recv(1024)
    # print('命令结果大小: ',cmd_res_size,type(cmd_res_size))
    # client.send(b'ack')
    # received_size = 0
    # received_data = b''
    # while received_size != int(cmd_res_size):
    #     data = client.recv(1024)
    #     received_size += len(data)
    #     received_data += data
    #
    # else:
    #     print("cmd res receive done ...",received_size)
    #     print(received_data.decode())
client.close()

