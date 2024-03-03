import json
import socket

from utils.response import parse_response as response
from utils.request import unparse_request as request 


config = json.load(open("config.json"))


sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((config['host'], config['port']))
sock.listen(config['max-connection'])


def sock_headler():
    while True:
        connection, _ = sock.accept()

        req = request(connection.recv(1028).decode())

        for r in response(req):
            connection.send(r.encode())
        connection.close()

def main():
    sock_headler()

if __name__ == "__main__":
    main()



