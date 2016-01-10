import urllib.request
from bs4 import BeautifulSoup

url = "http://finance.yahoo.com/q/ks?s=SBUX+Key+Statistics"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")
table = soup.find("table", border=0, cellspacing = 1)

for row in table.findAll('tr'):
    col = row.findAll('td')
    #print(col[0])
    value1 = str(col[0])
    value1 = value1[40:]
    i = 0
    while (value1[i]!="<" and value1[i]!=":"):
        i=i+1
    value1 = value1[:i]
    print(value1)
    
    #print(col[1])
    value2 = str(col[1])
    value2 = value2[28:]
    if (value1 == "Market Cap (intraday)"):
        value2 = value2[24:-12]
    else:
        value2= value2[:-5]
    print (value2)




