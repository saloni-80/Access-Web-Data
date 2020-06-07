import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url= input("Enter location: " )
data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data.decode())
lst = tree.findall('.//comment')
print('User count:', len(lst))

num=list()
for item in lst:
    num.append(item.find('count').text)
num=[int(i) for i in num]
print ("Sum ", sum(num))
