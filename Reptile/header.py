import requests
hd = {'User-agent': '123'}
r = requests.get('http://www.neverchange.com', headers=hd)
print(r)
