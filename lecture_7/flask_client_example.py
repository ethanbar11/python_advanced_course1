import requests

ip = 'http://127.0.0.1:5000/new_user/{}'
ip_woho = 'http://127.0.0.1:5000/woho'
# r=requests.get(ip.format('Ethan'))
r = requests.post(ip_woho, json={'Bla bla': 5, 'Bli blo': 8})
# r = requests.get(ip.format(''))
# r2 = requests.post(ip.format('blibla'))
print(r, r.content.decode())
# print(r2,r2.content.decode())
