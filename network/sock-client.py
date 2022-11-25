import socket
import time

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.bind(("10.4.155.92", 5555))
s.listen(1)
conn, info = s.accept()
msg = conn.recv(1024)
print(msg)

if msg == b'id\r\n':
    print("6410545461\r\n")
    conn.send(b'6410545461\r\n')
if msg == b'name\r\n':
    print("RESP : Happy \r\n")
    conn.send(b'Happy\r\n')
time.sleep(0.3)
s.close()
