import socket

HEADER = 512
PORT = 8080
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print("Msg Recieved:")
    print(client.recv(2048).decode(FORMAT))

def start():
    print("Send gretting to server")
    send("GET /HTTP/1.1 greetings from client")
    input()
    contiLoop = True
    while contiLoop:
        print("To add item in Alice School bag enter 1 for exit enter 0\n")
        qr = input("Enter Value:")
        if(qr == 0):
            contiLoop = False
        item = input("Add item to school bag:")
        finalmsg = "POST /HTTP/1.1 " + item
        print(finalmsg)
        send(finalmsg)
        input()
    
    send(DISCONNECT_MESSAGE)
    

start()

