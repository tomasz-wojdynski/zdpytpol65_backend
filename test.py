import requests

response = requests.get('https://www.wp.pl')
print(response.text)
