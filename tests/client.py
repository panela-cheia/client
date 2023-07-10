import requests

class WebClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path, params=None):
        url = self.base_url + path
        response = requests.get(url, params=params)
        return response

    def put(self, path, data=None):
        url = self.base_url + path
        response = requests.put(url, data=data)
        return response

    def delete(self, path):
        url = self.base_url + path
        response = requests.delete(url)
        return response

    def post(self, path,headers=None,data=None, files=None):
        url = self.base_url + path

        response = requests.post(url, headers=headers,data=data, files=files)
        return response

client = WebClient('http://localhost:3333')

files = {'file': open('/home/luciano/Documentos/Github/panela-cheia/client/tests/sushi.jpg', 'rb')}  # Replace with the actual file path

response = client.post('/files', files=files)
print(response.status_code)  # Status code of the response
print(response.text)  # Response body