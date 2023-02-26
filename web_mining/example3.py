from bs4 import BeautifulSoup
import requests

url = 'https://www.flipkart.com/search?q=shoes&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_6_5_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_6_5_na_na_na&as-pos=6&as-type=RECENT&suggestionId=shoes&requestId=42ec13c2-2d83-464a-a740-46a6af515b9c&as-searchtext=shoes'
response = requests.get(url)
if not response.status_code == 200:
    print('An error has occured.')
    exit()