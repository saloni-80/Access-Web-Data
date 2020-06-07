import urllib.request, urllib.parse, urllib.error
import json

url= input("Enter location: " )
data = urllib.request.urlopen(url).read()

info = json.loads(data.decode())
lst = info['comments']
print('User count:', len(lst))

num=list()
for item in lst:
    num.append(item['count'])
num=[int(i) for i in num]
print ("Sum ", sum(num))
