import socket


def serverfunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    addr = ("127.0.0.1",7852)
    sock.bind(addr)
    date, addr = sock.recvfrom(500)
    date = date.decode()
    print(type(date))
    print(date)

    t = "i have recieved your message"
    date = t.encode()
    sock.sendto(date, addr)



if __name__ == "__main__":
    print("starting server")
    serverfunc()
    print("ending server")