import sys
import time
import socket

#now creating a socket
def create_socket():
    try:
        global host
        global port
        global s
        host=""
        port=9999
        s=socket.socket()
    except socket.error as msg:
        print(str(msg))

#binding the socket and listen for the connection
#means need to bind the host and the port
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port : ",str(port))
        s.bind((host,port))
        #no. of connection it would tolerate to listen ...
        n=5
        s.listen(n)


    except socket.error as msg:
        print(str(msg)+"\n"+"retrying ....")
        bind_socket()

#establist the  connection with the client and socket must be listening

def socket_accect():
    connection,address=s.accept()
    print("Connection has been established : "+"IP "+address[0]+"port "+str(address[1]))
    #the function wchich run the commands run on client side
    send_command(connection)
    #end of acception
    connection.close()
def send_command(conn):
    while True:
        cmd=input()
        if cmd=="quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            #sending the command :
            conn.send(str.encode(cmd))
            #chunk standard size 1024
            client_response=str(conn.recv(1024),"utf-8")
            print("Client response is ",client_response,end="")

def main():
    create_socket()
    bind_socket()
    socket_accect()

main()
