from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
 
import pandas as pd 
import time
URL =  "https://webscraper.io/test-sites/e-comerce/ajax/computers/laptops"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
driver.get (URL) 
time.sleep(3) 
products = driver.find_elements(By.CLASS_NAME, "thumbnail") 
data = [] 
for product in products:
    title = product.find_element(By.CLASS_NAME , "title").text
    price = product.find_element(By.CLASS_NAME , "price").text
    link = product.find_element(By.CLASS_NAME, "title").get_attribute("href") 
    print(f"{title} {price} {link}")
    data.append({"Title" : title, "Price": price, "Link": link}) 
pd.Dataframe(data).to_csv("laptops.csv", index=False) 
print("\n scraping complete Data saved to laptops.csv")
driver.quit()