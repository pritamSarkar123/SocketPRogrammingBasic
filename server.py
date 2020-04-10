import socket
import threading
import pickle #for sending serialized obj through server

HEADER=64 #64byte
FORMAT = 'utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"
PORT = 5050  #local host port no
#SERVER = "192.168.0.6"  #my computers Local IPv4
#OR
SERVER = socket.gethostbyname(socket.gethostname())#use public IP for connecting through internet

ADDR = (SERVER, PORT)  #tuple for binding
#server is the new socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#runs concurrently for each client
def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected')
    connected = True
    while connected:
        #blocking line of code
        #waits for a message from client
        #it waits untill a message comes
        msg_length=conn.recv(HEADER).decode(FORMAT) #how many bytes we are gona receive
        if msg_length: #if somthing valid comes
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected=False
            print(f"[{addr} {msg}]")
            conn.send(f"MEssage received from {addr} by {SERVER}".encode(FORMAT)) #resending message to client
    conn.close()

#start the socket server for us
#allow our server for start listning new connections
#handling those connections 
#passing those to handle_client function
def start():
    server.listen()
    print(f"[LISTNING] Server is listning on {SERVER}")
    while True:
        #it blocks
        #it waits for a new connection to the server
        #when the new connection occurs
        #sotore its Object(conn) and address(IP and port)
        #conn is object, used for communication(socket obj)
        conn, addr = server.accept()#server accepted a connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        #shows no of active connections except start thread
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")

if __name__=="__main__":
    print("[STARTING] server is starting...")
    start()