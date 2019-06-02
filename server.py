#server
import socket
sock = socket.socket()
sock.bind(("", 9090))
sock.listen(1)
conn, addr = sock.accept()
matrix = []
lmat = conn.recv(1024).decode()
lmat = lmat.replace(" ", ";").replace(";;", ";").split(";",)
i = 0
while i < len(lmat):
    matrix.append(lmat[i])
    i+=1
#считаю определитель
A = int(matrix[0])*int(matrix[4])*int(matrix[8])+int(matrix[1])*int(matrix[5])*int(matrix[6])+\
int(matrix[2])*int(matrix[3])*int(matrix[7])-int(matrix[2])*int(matrix[4])*int(matrix[6])-\
int(matrix[0])*int(matrix[5])*int(matrix[7])-int(matrix[1])*int(matrix[3])*int(matrix[8])

#отправляю клиенту
conn.send(str(A).encode())

conn.close()
