import socket
client = socket.socket()
client.connect(('www.python.org',80))
message = 'GET / HTTP/1.1\r\nHOST:www.python.org\r\nConnection:close\r\n\r\n'
print('connect')
client.send(message.encode())
data = client.recv(1024)
print(data)
client.close()