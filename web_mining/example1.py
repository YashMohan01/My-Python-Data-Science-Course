import requests

url ="https://www.google.com/search?=python"
response = requests.get(url)
if response.status_code == 200:
    print('Success!')
    print(response.text)
else:
    print('An error has occured')