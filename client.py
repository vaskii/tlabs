#client
import socket
sock = socket.socket()
sock.connect(("localhost", 9090))
print("Введите матрицу в виде:\na11, a12, a13; a21, a22, a23; a31, a32, a33")
a = input(">>> ")
sock.send(a.encode())
data = sock.recv(1024).decode()

sock.close()

print("Определитель = " + data)
