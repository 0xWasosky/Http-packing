import socket



s = socket.socket()


s.connect(("localhost", 5001))


s.send(b"GET /home")

print(s.recv(8042))