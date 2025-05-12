from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com/scroll")
time.sleep(2)

all_quotes = set()  # To store unique quotes

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Get all quotes on the page
    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    
    # Extract quote text and author for each quote
    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, "text").text  # Extracting quote text
        author = quote.find_element(By.CLASS_NAME, "author").text  # Extracting author name
        full_quote = f"{text} - {author}"  # Combining both text and author
        all_quotes.add(full_quote)  # Add the full quote to the set
    
    # Scroll to the bottom to load more quotes
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the new quotes to load
    
    # Check the new page height
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    # If no new content is loaded (height remains the same), break the loop
    if new_height == last_height:
        break
    
    last_height = new_height

# Print all the unique quotes collected
for quote in all_quotes:
    print(quote)

driver.quit()
