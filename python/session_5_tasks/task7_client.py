import socket 


PORT = 5050
SERVER = '127.0.0.1' #socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print(client.recv(1024).decode(FORMAT))

message = {"id" : "xyz", "Value": 385, "type" : "Temperature"}

send(str(message))
input()
send(DISCONNECT_MESSAGE)
