# Assignment Selenium

This directory contains completed assignment "PSelenium". All exercises performent in PyCharm.

## Contents

- All the finished exercises of assigment "Seleinium" are in the file [search.py](./search.py)

## Tasks

1. **Open Browser:**
  * Navigate to URL ( www.ebay.com )
  * Print URL
  * Close browser
2. **Add wait:**
  * Navigate to URL ( www.ebay.com )
  * WebDriverWait -  Waiting for the page to load 
  * Print URL
  * Close browser
3. **Search items:**
  * Navigate to URL ( www.ebay.com )
  * WebDriverWait -  Waiting for the page to load 
  * Print URL
  * Type “women watch” into search field
  * Press search
  * Close browser
4. **Verify the search results:**
  * Navigate to URL ( www.ebay.com )
  * WebDriverWait -  Waiting for the page to load 
  * Print URL
  * Type “women watch” into search field
  * Press search
  * Verify the header contains “results for women watch“
  * Close browser

## Comments

Printed extra messages to make the output more informative.
```python
...
print('Waiting for the page to load...')
...
print(f"The page has been loaded. Current url is: {driver.current_url}")
...
print(f"Searching for \"{search_input}\"...")
...
print(f"Found in header: {header_text}")
...
print('Verified. The header contains “results for women watch“')
...
```

