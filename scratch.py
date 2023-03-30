import base64
import requests

headers = {
    'content-type': 'multipart/form-data', 'Authorization': 'Token 973fad8e0f7368dd90a5277f5dba0b15a8c294d2'
}
# read the binary file and encode it as Base64
data = {
    "business": 1, "user": 1, "fingerprint": base64.b64encode(b'Hello World').decode('utf-8')
}

# make the API call
r = requests.post('http://localhost:8000/api/business/biometrics/', headers=headers, json=data)
print(r.text)