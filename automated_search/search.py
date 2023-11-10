from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from components.base import Base


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 100)

link = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0"
driver.get(link)
print('Waiting for the page to load...')
search_bar = wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@id="gh-ac"]')))
print(f"The page has been loaded. Current url is: {driver.current_url}")

rolex_link = """//span[@class="cbx x-refine__multi-select-cbx"][text()='Rolex']"""
wait.until(ec.element_to_be_clickable((By.XPATH, rolex_link))).click()
print("Filter by Brand/Rolex enabled")
print(f"The page has been loaded. Current url is: {driver.current_url}")

result1 = """//li[@class="s-item s-item__pl-on-bottom" and @data-gr4="1"]"""
result2 = """//li[@class="s-item s-item__pl-on-bottom" and @data-gr4="3"]"""

title1 = wait.until(ec.visibility_of_element_located((By.XPATH, result1 + '//span[@role="heading"]')))
print("Result 1 is visible")
title2 = wait.until(ec.visibility_of_element_located((By.XPATH, result2 + '//span[@role="heading"]')))
print("Result 2 is visible")

title1_text = title1.text
print(f"Found in header of first result: {title1_text}"
      f"\n{'Verified. The title contains “rolex“' 
      if 'rolex' in title1_text.lower() else 'No \'rolex\' in the title'}")
price_line1 = wait.until(ec.visibility_of_element_located((
      By.XPATH, result1 + '//span[@class="s-item__price"]')))
price1_search_results = price_line1.text
print(price1_search_results)
title2_text = title2.text
print(f"Found in header of second result: {title2_text}"
      f"\n{'Verified. The title contains “rolex“' 
      if 'rolex' in title2_text.lower() else 'No \'rolex\' in the title'}")
price_line2 = wait.until(ec.visibility_of_element_located((
      By.XPATH, result2 + '//span[@class="s-item__price"]')))
price2_search_results = price_line2.text
print(price2_search_results)

print("checking item #1")
driver.find_element(By.XPATH, result1 + '//span[@role="heading"]').click()

# Switch to the new tab
new_tab_handle = driver.window_handles[-1]  # Assuming the new tab is the last one opened
driver.switch_to.window(new_tab_handle)

title_item_page = wait.until(ec.visibility_of_element_located((By.XPATH, """//div[@id="mainContent"]//h1//span[@class="ux-textspans ux-textspans--BOLD"]""")))
title1_item_page = title_item_page.text
print(f"Title of the first item on the item page is: {title1_item_page}")

price_line_item_page = wait.until(ec.visibility_of_element_located((By.XPATH, """//div[@id="mainContent"]//*[@class="x-price-primary"]/span[@class="ux-textspans"]""")))
price1_item_page = price_line_item_page.text
print(f"Price of the first item on the item page is: {price1_item_page}")
driver.close()

new_tab_handle = driver.window_handles[0]  # Assuming the new tab is the last one opened
driver.switch_to.window(new_tab_handle)

print("checking item #2")
driver.find_element(By.XPATH, result2 + '//span[@role="heading"]').click()

# Switch to the new tab
new_tab_handle = driver.window_handles[-1]  # Assuming the new tab is the last one opened
driver.switch_to.window(new_tab_handle)

title_item_page = wait.until(ec.visibility_of_element_located((By.XPATH, """//div[@id="mainContent"]//h1//span[@class="ux-textspans ux-textspans--BOLD"]""")))
title2_item_page = title_item_page.text
print(f"Title of the second item on the item page is: {title2_item_page}")

price_line_item_page = wait.until(ec.visibility_of_element_located((By.XPATH, """//div[@id="mainContent"]//*[@class="x-price-primary"]/span[@class="ux-textspans"]""")))
price2_item_page = price_line_item_page.text
print(f"Price of the second item on the item page is: {price2_item_page}")
driver.close()

new_tab_handle = driver.window_handles[0]  # Assuming the new tab is the last one opened
driver.switch_to.window(new_tab_handle)

print("Comparing the title of the first item on the search page with the one on the item page... "
      "Titles of the first item MATCH" if title1_text == title1_item_page else "Titles of the first item ARE DIFFERENT")

print("Comparing the title of the second item on the search page with the one on the item page... "
      "Titles of the second item MATCH" if title2_text == title2_item_page else "Titles of the second item ARE DIFFERENT")

def transform_to_integer(string):
    string = string.replace("US $", "").replace("$", "").replace(",", "")
    return int(float(string))


price1_search_results_cleaned = transform_to_integer(price1_search_results)
price1_item_page_cleaned = transform_to_integer(price1_item_page)

print("Comparing the price of the first item on the search page with the one on the item page... "
      "Prices of the first item MATCH" if price1_search_results_cleaned == price1_item_page_cleaned else "Prices of the first item ARE DIFFERENT")

price2_search_results_cleaned = transform_to_integer(price2_search_results)
price2_item_page_cleaned = transform_to_integer(price2_item_page)

print("Comparing the price of the second item on the search page with the one on the item page... "
      "Prices of the second item MATCH" if price2_search_results_cleaned == price2_item_page_cleaned else "Prices of the second item ARE DIFFERENT")