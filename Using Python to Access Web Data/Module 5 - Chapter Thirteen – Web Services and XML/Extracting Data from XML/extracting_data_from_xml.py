import urllib.request
import xml.etree.ElementTree as ET
# Assignment data URL:
# https://py4e-data.dr-chuck.net/comments_2334052.xml
url = input('Enter location: ')
if len(url) < 1 : 
    url = 'https://py4e-data.dr-chuck.net/comments_2334052.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')
nums = list()
for result in counts:
    print(result.text)
    nums.append(int(result.text))
print('Count:', len(nums))
print('Sum:', sum(nums))