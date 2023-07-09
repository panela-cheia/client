import http.client

class WebClient:
    def __init__(self, host):
        self.host = host
        self.connection = http.client.HTTPSConnection(host)

    def request(self, method, path):
        self.connection.request(method, path)
        response = self.connection.getresponse()
        return response