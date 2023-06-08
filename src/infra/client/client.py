import socket
import json

aux16 = {
    "topic": "@recipe/list_recipe",
    "body": {
    }
}

class Client:
    def __init__(self) -> None:
       # self.SERVER = '127.0.0.1'
        self.SERVER = '172.18.0.1'
        self.PORT = 3031
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