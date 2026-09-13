from urllib.request import urlopen
from bs4 import BeautifulSoup
# Assignment starting URL:
# https://py4e-data.dr-chuck.net/known_by_Pyper.html
# Assignment count: 7
# Assignment position: 18
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))
for i in range(count):
    print("Retrieving", url)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    target_tag = tags[position - 1] 
    name = target_tag.contents[0]
    url = target_tag.get('href', None)