from others import Client
import json

response = Client().test()

# print(response[0]["id"])

print(json.dumps(response,indent=4,ensure_ascii=False))


'''
# POST request with a file and additional fields
form_data = {
    'file': {
        'filename': 'sushi.jpg',
        'content_type': 'application/json',
        'data': 'file',
    }
}
response = client.request('POST', '/files', form_data=form_data)

print(response.status)    # Status code of the response
print(response.read())    # Raw response data
'''