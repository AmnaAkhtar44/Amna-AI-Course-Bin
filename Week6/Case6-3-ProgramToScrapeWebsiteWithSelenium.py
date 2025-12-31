from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url ="http://www.values.com/inspirational-quotes"
cService = webdriver.ChromeService(executable_path='C:\\Users\\ORACLE\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)

driver.get(url)
qouestList=[]
qoutesDiv = driver.find_elements(By.XPATH, "//div[contains(@class, 'text-center mb-8')]")
for p in range(len(qoutesDiv) -1):
    quote = {}
    innerImg = qoutesDiv[p+1].find_element(By.TAG_NAME, "img")
    innera = qoutesDiv[p+1].find_element(By.TAG_NAME, "a")
    quote["img"] =innerImg.get_attribute('src') 
    quote["lines"] =innerImg.get_attribute('alt') 
    quote['url'] = innera.get_attribute('href')
    qouestList.append(quote)

filename = 'Amna-AI-Course-Bin/Week6/inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['img','lines','url'])
    w.writeheader()
    for quote in qouestList:
        w.writerow(quote)

driver.close()