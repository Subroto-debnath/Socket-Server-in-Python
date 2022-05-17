import socket 
import threading


HEADER = 512
PORT = 8080
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname()) 
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

bag =["Book", "Pen"]
inittialMsg = "Alice school bag contains:"


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        match = ["GET", "greetings"]
        
        msg_length = conn.recv(HEADER).decode(FORMAT)
        print(msg_length)
        if msg_length:
            
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            
            
            if msg == DISCONNECT_MESSAGE:
                connected = False
                
            if any(x in msg for x in match):
                print(f"[{addr}] {msg}")
                conn.send("Greeting from server".encode(FORMAT))
                item = " "
                for i in bag:
                    item = item + i + " "
                finalMsg = inittialMsg + item
                conn.send(finalMsg.encode(FORMAT))
            elif "GET"  in msg:
                print(f"[{addr}] {msg}")
                conn.send("GET Request Received".encode(FORMAT))   
            elif "POST" in msg:
                print(f"[{addr}] {msg}")
                strlen = len(msg)
                newItem = msg[15:strlen]
                bag.append(newItem)
                print(bag)
                item = " "
                for i in bag:
                    item = item + i + " "
                finalMsg = inittialMsg + item
                conn.send(finalMsg.encode(FORMAT))
            else:    
                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))

    conn.close()
        

def start():
    server.listen(8080)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()



#References
#https://realpython.com/python-sockets/
#https://www.edureka.co/blog/socket-programming-python/
#https://www.edureka.co/blog/socket-programming-python/
#https://docs.python.org/3/howto/sockets.html



