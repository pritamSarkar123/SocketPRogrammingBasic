import socket
HEADER=64 #64byte
FORMAT = 'utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"
PORT = 5050  #local host port no
SERVER = socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#use public IP for connecting through internet
client.connect(ADDR) #no binding needed on client side

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(msg.encode(FORMAT))
    print(client.recv(2048).decode(FORMAT))  #2048 assumed length of the server message

if __name__=="__main__":   
    send("hello world!")
    input()
    send("hello world!")
    input()
    send("hello world!")
    input()
    send("hello world!")
    input()
    send("hello world!")
    send(DISCONNECT_MESSAGE)