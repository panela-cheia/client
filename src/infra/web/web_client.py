import requests

class WebClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path, params=None):
        url = self.base_url + path
        response = requests.get(url, params=params)
        return response

    def put(self, path,headers=None,data=None):
        url = self.base_url + path
        
        response = requests.put(url, data=data,headers=headers)
        return response

    def delete(self, path):
        url = self.base_url + path
        response = requests.delete(url)
        return response

    def post(self, path,headers=None,data=None, files=None):
        url = self.base_url + path

        response = requests.post(url, data=data, headers=headers,files=files)
        return response