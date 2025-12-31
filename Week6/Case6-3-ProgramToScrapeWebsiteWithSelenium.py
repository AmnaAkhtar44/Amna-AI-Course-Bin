"""from selenium import webdriver
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

driver.close()"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# =========================
# URL
# =========================
url = "http://www.values.com/inspirational-quotes"

# =========================
# Chrome Options
# =========================
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.page_load_strategy = "eager"

# =========================
# Chrome Service
# =========================
service = Service(
    executable_path=r"C:\Users\ORACLE\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
)

driver = webdriver.Chrome(service=service, options=options)
driver.set_page_load_timeout(300)

# =========================
# Open Website
# =========================
driver.get(url)

# =========================
# Explicit Wait (VERY IMPORTANT)
# =========================
wait = WebDriverWait(driver, 20)

quotesDiv = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//div[contains(@class, 'text-center mb-8')]")
    )
)

# =========================
# Scraping Logic
# =========================
quotesList = []

for div in quotesDiv:
    try:
        quote = {}

        img = div.find_element(By.TAG_NAME, "img")
        a_tag = div.find_element(By.TAG_NAME, "a")

        quote["img"] = img.get_attribute("src")
        quote["lines"] = img.get_attribute("alt")
        quote["url"] = a_tag.get_attribute("href")

        quotesList.append(quote)

    except Exception:
        continue

# =========================
# Save to CSV
# =========================
filename = r"Amna-AI-Course-Bin\Week6\inspirational_quotes.csv"

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["img", "lines", "url"])
    writer.writeheader()
    writer.writerows(quotesList)

# =========================
# Close Browser
# =========================
driver.quit()

print(f"Scraped {len(quotesList)} quotes successfully.")
