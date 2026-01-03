from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import os


url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"
cService = webdriver.ChromeService(executable_path='C:\\Users\\ORACLE\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)

driver.get(url)
qouestList=[]
qoutesDiv = driver.find_elements(By.XPATH, "//div[contains(@class, 'brwrvr__item-card brwrvr__item-card--1 brwrvr__item-card--list brwrvr__item-card--compare')]")
for p in range(len(qoutesDiv) -1):
    quote = {}
    innerImg = qoutesDiv[p+1].find_element(By.TAG_NAME, "img")
    quote["img"] =innerImg.get_attribute('src') 
    quote["lines"] =innerImg.get_attribute('alt') 
    quote["author"] =innerImg.get_attribute('style') 
    qouestList.append(quote)


filename = 'WebScrapPractice/ebay_quotesMethod3.csv'

os.makedirs(os.path.dirname(filename), exist_ok=True)

with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(
        f,
        fieldnames=['img','lines','author']
    )
    writer.writeheader()

    writer.writerow({
        'img': 'image1.jpg',
        'lines': 'Sample quote',
        'author': 'Unknown'
    })

    
driver.close()