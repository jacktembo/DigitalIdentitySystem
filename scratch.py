import requests
headers = {
    'Authorization': 'Token 7f63f956e09392d2ce47c85a70c1992b94b0ca8b'
}
data = {'user': 2}
r = requests.post('http://localhost:8000/users/details/2/', json=data, headers=headers)
print(r.text)