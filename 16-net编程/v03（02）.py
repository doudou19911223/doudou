
import socket


def clientfunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    text = "i love jingjing"
    date = text.encode()

    sock.sendto(date, ("127.0.0.1",7852))
    date, addr = sock.recvfrom(200)
    date = date.decode()
    print(date)


if __name__ == "__main__":
    clientfunc()