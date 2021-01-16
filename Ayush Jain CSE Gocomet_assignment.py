//Create a scrapping/crawling application that can crawl medium.com
import requests
from bs4 import BeautifulSoup
url"https://medium.com"
r=requests.get(url)
htmlContent=r.Content
s=BeautifulSoup(htmlContent,'html.parser')
print(s.prettify)
#get the title
gocomettitle=s.title
#get all paragraphs
paragraphs=s.find_all('p')
anchors=s.find_all('a')
#get the text elements from the page
print(s.find('p').get_text())
print(s.get_text())
anchors=s.find_all('a')
all_links=set()
#for all links in medium.com
for link in anchors:
    if(link.get('href')!="#"):
        linkText="https://medium.com" + link.get('href')
        all_links.add(link)

root_of_scrapp=s.find(id='root')
for elements in root_of_scrapp.contents:
    print(elements)
