import socket
import json

aux16 = {
    "topic": "@recipe/list_recipe",
    "body": {
    }
}

from config.app_url import HOST,PORT

class Client:
    def __init__(self) -> None:
        self.SERVER = HOST
        self.PORT = PORT
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dest = (self.SERVER, self.PORT)

    def send(self, message: str):
        EOF = 0x05
        self.tcp.send(message.encode())
        self.tcp.send(bytearray([EOF]))

    def read(self) -> str:
        message = ""
        EOF = 0x05
        while True:
            msg = self.tcp.recv(4096)
            if not msg:
                break
            if msg[len(msg) - 1] == EOF:
                message += str(msg[: len(msg) - 1].decode())
                break
            else:
                message += str(msg.decode())
        return message
    
    def connect(self):
        self.tcp.connect(self.dest)

    def close(self):
        self.tcp.close()

    def test(self):
        self.tcp.connect(self.dest)
        message = json.dumps(aux16)
        self.send(message=message)
        message = self.read()
       
        if not message:
            return None

        data = json.loads(message)

        return data