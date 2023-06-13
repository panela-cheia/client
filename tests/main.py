from others import Client
import json

response = Client().test()

# print(response[0]["id"])

print(json.dumps(response,indent=4,ensure_ascii=False))