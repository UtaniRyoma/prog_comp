import sys, socket, select


class ServerSocket:
    """Deal server sockert with not a main function but an object"""
    def __init__(self, port = 5001,  socklist = [], server = '127.0.0.1', serversock = None):
#    def __init__(self, port = 5001,  socklist = [], server = socket.gethostname()):
        # create an INET, STREAMing socket
        self.port = port
        self.socklist = socklist
        self.server = server
        if serversock is None:
            self.serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.serversock = serversock

    def bindsock(self, listen = 10):
        self.serversock.bind((self.server, self.port))
        self.serversock.listen(listen)

    def appendsock(self, sock = None):
        if sock == None:
            self.socklist.append(self.serversock)
        else:
            self.socklist.append(sock)

    def broadcast(self, sock, message):
        print(message)
        for socket in self.socklist:
            if socket != self.serversock and socket != sock :
                try :
                    socket.send(message.encode())
                except :
                    socket.close()
                    self.socklist.remove(socket)

if __name__ == '__main__':
    # port, socklist, server = 5001, [], '127.0.0.1' if len(sys.argv) <= 1 else sys.argv[1]
    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket.bind((server, port))
    # server_socket.listen(10)
    # socklist.append(server_socket)
    print('Start')
    while True:
        read_sockets, write_sockets, error_sockets = select.select(socklist, [], [])
        for sock in read_sockets:
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                socklist.append(sockfd)
                broadcast(socklist, server_socket, sockfd, '[%s:%s] Enter' % addr)
            else:
                try:
                    data = sock.recv(4096).decode()
                    if data == '': raise Exception('Done')
                    if data:
                        broadcast(socklist, server_socket, sock, data)
                except Exception as e:
                    print(e)
                    broadcast(socklist, server_socket, sock, '[%s, %s] Exit' % addr)
                    sock.close()
                    socklist.remove(sock)
