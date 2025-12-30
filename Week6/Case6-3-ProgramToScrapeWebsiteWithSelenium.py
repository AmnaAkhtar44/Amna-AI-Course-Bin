from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import os

url = "http://www.values.com/inspirational-quotes"

cService = webdriver.ChromeService(executable_path='C:\\Users\\ORACLE\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe') # '/Users/bpfalz/Downloads/chromedriver' for my macbook
driver = webdriver.Chrome(service=cService)

#driver.get(url)

try:
    driver.get(url)

    # 2. Scraping Logic
    qouestList = []
    # Using a slightly more specific XPATH to ensure we get the quote containers
    qoutesDiv = driver.find_elements(By.XPATH, "//div[contains(@class, 'text-center mb-8')]")

    for p in range(len(qoutesDiv) - 1):
        quote = {}
        try:
            # We use p+1 because the first element in this specific list is often a header/empty
            container = qoutesDiv[p+1]
            innerImg = container.find_element(By.TAG_NAME, "img")
            innera = container.find_element(By.TAG_NAME, "a")
            
            quote["img"] = innerImg.get_attribute('src') 
            quote["lines"] = innerImg.get_attribute('alt') 
            quote['url'] = innera.get_attribute('href')
            qouestList.append(quote)
        except Exception as e:
            continue # Skip any elements that don't match the expected structure

    # 3. File & Folder Handling
    filename = 'Week6/inspirational_quotesMethod2.csv'
    directory = os.path.dirname(filename)

    # This creates the 'Week6' folder if it doesn't exist
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

    # 4. Writing to CSV
    # Added encoding='utf-8' to prevent errors with special characters in quotes
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        # Fieldnames must match the keys in your 'quote' dictionary exactly
        w = csv.DictWriter(f, fieldnames=['url', 'img', 'lines'])
        w.writeheader()
        w.writerows(qouestList)

    print(f"Success! Saved {len(qouestList)} quotes to {filename}")
finally:
    # 5. Cleanup
 driver.quit()