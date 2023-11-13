# Assignment Automated Search

This directory contains completed assignments "Automated Search". 
All exercises performed in PyCharm editor.

## Contents

- The main file to run is [search.py](./search.py)
- Basic operations with the browser are in the file: [components/base.py](./components/base.py)
- Operations with Search Results Page are in the file: [components/search_results_page.py](./components/search_results_page.py)
- Operations with Left Panel in Search Result Page are in the file: : [components/left_filter_panel.py](./components/search_results_page.py)
- Operations with Item Page are in the file: [components/item_page.py](./components/item_page.py)
- Verification function and logger are in the file: [components/verification.py](./components/verification.py)

## Tasks for "Automated Search" assigment

1. Open eBay watch page ( watch for sale | eBay  )
2. Select option Brand / Rolex in Filter panel
3. Verify the first two result items contain “rolex” in their title
4. Store title and price of the first two results in a variable
5. Open item in and verify the title and the price by comparing them with the stored data
6. Uncheck “Rolex“ option
7. Check “Casio“ option
8. Verify the last two result items contain “Casio“ in their title
9. Save and print all the mismatches if any

## Updates

Update 11/13/23:
1. Moved LeftFilterPanel class to separate module [components/left_filter_panel.py](./components/left_filter_panel.py)
2. Renamed `MISMATCH` variable to lower case `mismatch` from [components/verification.py](./components/verification.py) module according to PEP 8
3. Renamed [components/item_page.py](./components/item_page.py) module according to PEP 8
4. Renamed [components/search_results_page.py](./components/search_results_page.py) according to PEP 8
5. Moved all locators that were defined Class variables back to methods