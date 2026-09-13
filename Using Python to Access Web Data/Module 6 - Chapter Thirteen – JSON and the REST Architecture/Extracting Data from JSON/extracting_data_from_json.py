import urllib.request
import json
# Assignment data URL:
# https://py4e-data.dr-chuck.net/comments_2334053.json
url = input('Enter location: ')
if len(url) < 1 :
    url = 'https://py4e-data.dr-chuck.net/comments_2334053.json'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved',len(data),'characters')
js = json.loads(data)
nums = list()
for item in js['comments']:
    print(item['count'])
    nums.append(item['count'])
print('count:', len(nums))
print('sum:', sum(nums))