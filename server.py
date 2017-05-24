import sys, socket, select
from socket_lib import ServerSocket

if __name__ == '__main__':
    server = ServerSocket(5001, [], '127.0.0.1')
    server.bindsock(10)
    server.appendsock()
    print('Start')
    while True:
        read_sockets, write_sockets, error_sockets = select.select(server.socklist, [], [])
        for sock in read_sockets:
            if sock == server.serversock:
                sockfd, addr = server.serversock.accept()
                server.appendsock(sockfd)
                server.broadcast(sockfd, '[%s:%s] Enter' % addr)
            else:
                try:
                    data = sock.recv(4096).decode()
                    if data == '': raise Exception('Done')
                    if data:
                        server.broadcast(sock, data)
                except Exception as e:
                    print(e)
                    server.broadcast(sock, '[%s, %s] Exit' % addr)
                    sock.close()
                    server.socklist.remove(sock)
