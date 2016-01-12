import urllib.request
from bs4 import BeautifulSoup

def getStats(url):
    #url = "http://finance.yahoo.com/q/ks?s=SBUX+Key+Statistics"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    #print(soup.prettify())
    #stats=soup.find_all('td',class_='yfnc_tablehead1')
    table = soup.find("table", border=0, cellspacing = 1)
    elements = []
    index = 0
    for row in table.findAll('tr'):
        col = row.findAll('td')
        #print(col[0])
        value1 = str(col[0])
        value1 = value1[40:]
        i = 0
        while (value1[i]!="<" and value1[i]!=":"):
            i=i+1
        value1 = value1[:i]
        #print(value1)
        
        #print(col[1])
        value2 = str(col[1])
        value2 = value2[28:]
        if (value1 == "Market Cap (intraday)"):
            value2 = value2[24:-12]
        else:
            value2= value2[:-5]
        #print (value2)
        
        elements.append([])
        elements[index].append(value1)
        elements[index].append(value2)
        index = index + 1
        
    return elements





