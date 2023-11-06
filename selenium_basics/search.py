from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://ebay.com")
print('Waiting for the page to load...')
search_bar = wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@id="gh-ac"]')))
print(f"The page has been loaded. Current url is: {driver.current_url}")

search_input = "women watch"
print(f"Searching for \"{search_input}\"...")
search_bar.send_keys('women watch')
search_bar.send_keys(Keys.RETURN)

header = wait.until(ec.visibility_of_element_located(
    (By.XPATH, "//h1[contains(@class, 'count-heading')]")))
header_text = header.text
print(f"Found in header: {header_text}")
assert f"results for {search_input}" in header_text
print('Verified. The header contains “results for women watch“')
driver.quit()
