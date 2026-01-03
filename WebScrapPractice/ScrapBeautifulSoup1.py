#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
 
URL = "https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
quotes=[]  # a list to store quotes   class="text-center mb-8"
 
table = soup.find('div', attrs = {'id':'beacon-aplus'}) 
 
for row in table.find_all('div',
                         attrs = {'class' : "daraz"}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" ")[0]
    quote['author'] = row.img['alt'].split(" ")[1]
    quotes.append(quote)
 
filename = 'WebScrapPractice/daraz.pk.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)