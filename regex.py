import re
file = open("content.txt")
num=list()
for line in file:
    line=line.rstrip()
    y=re.findall('[0-9]+',line)
    y=[int(i) for i in y]
    num.append(sum(y))
print (sum(num))
