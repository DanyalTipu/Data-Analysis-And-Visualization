from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

s = Service("chromedriver.exe")

driver = webdriver.Chrome(service = s)

driver.get("https://quotes.toscrape.com/")

quotes = driver.find_elements(By.CLASS_NAME, "quote")
print(len(quotes))

for quote in quotes:
    quote_list = driver.find_elements(By.CLASS_NAME,'text')

all_quotes=[]
print(len(quote_list))  
for x in range(0,(len(quotes))):
    if(x!='â€œ'):
        all_quotes.append(quote_list[x].text.strip())
    
print(all_quotes)
#
quote_df = pd.DataFrame({'Quotes': all_quotes})

# Specify the CSV filename
csv_filename = 'quotes.csv'

# Save the DataFrame to the CSV file
quote_df.to_csv(csv_filename, index=False)





