# credits: https://www.learndatasci.com/tutorials/ultimate-guide-web-scraping-w-python-requests-and-beautifulsoup/
import requests
from bs4 import BeautifulSoup

def automate_data_collection(urls):
  for i in urls:
    url = i
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup)

