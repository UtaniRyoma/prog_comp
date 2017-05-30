import sys, socket, select

class ServerSocket:
    """Deal server sockert with not a main function but an object"""
    def __init__(self, port = 5001,  socklist = [], server = socket.gethostname(), serversock = None):
#    def __init__(self, port = 5001,  socklist = [], server = socket.gethostname()):
        # create an INET, STREAMing socket
        self.port = port
        self.socklist = socklist
        self.server = server
        if serversock is None:
            self.serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.serversock = serversock

    def setPort(self, port):
        self.port = port

    def getPort(self, port):
        return self.port

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


class Client:
    def __init__(self, user_name, host_name = socket.gethostname(), port = 5001):
        self.user = user_name
        self.host = host_name
        self.port = port

    def setUser(self, user_name):
        self.user = user_name

    def getUser(self):
        return self.user

    def setHost(self, host_name):
        self.host = host_name

    def getHost(self):
        return self.host

    def setPort(self, port):
        self.port = port

    def getPort(self):
        return self.port
