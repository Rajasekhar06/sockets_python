import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISSCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.1.1"
ADDR =  (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send("Hello World!")
send(input())
send(DISSCONNECT_MESSAGE)



































'''import socket
HEADERSIZE = 16

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1254))

full_msg = ""
new_msg = True
while True:
    msg = s.recv(1024)
    if new_msg:
        print(f"new message length: {msg[:HEADERSIZE]}")
        msglen = int(msg[:HEADERSIZE])
        new_msg = False
    full_msg += msg.decode('utf-8')
    if len(full_msg)-HEADERSIZE == msglen:
        print("full message received")
        print(full_msg[HEADERSIZE:])
        new_msg = True
        full_msg = ''
print(full_msg)'''
    # print(msg.decode("utf-8"))