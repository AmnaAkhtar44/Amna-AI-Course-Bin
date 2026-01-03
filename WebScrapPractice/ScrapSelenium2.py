from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import os

url = "https://www.daraz.pk/catalog/?q=Smart%20Phones"

service = Service(r"C:\\Users\\ORACLE\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 30)

driver.get(url)

products = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//div[@data-qa-locator='fs-card-img']")
    )
)

data = []
for p in products:
    try:
        img = p.find_element(By.TAG_NAME, "img")
        data.append({
            "img": img.get_attribute("src"),
            "lines": img.get_attribute("alt"),
            "author": "Daraz"
        })
    except:
        pass

os.makedirs("C:/Temp", exist_ok=True)
with open("C:/Temp/daraz_products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["img", "lines", "author"])
    writer.writeheader()
    writer.writerows(data)

driver.quit()
print("Done")
