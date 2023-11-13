from automated_search.components.base import Base
from automated_search.components import verification
from automated_search.components.item_page import ItemPage
from automated_search.components.left_filter_panel import LeftFilterPanel
from automated_search.components.search_results_page import SearchResults

base = Base()  # Initializing Base class
left_filter_panel = LeftFilterPanel(base.driver, base.wait)  # Initializing LeftFilterPanel class
item_page = ItemPage(base.driver, base.wait)  # Initializing ItemPage class
search_results = SearchResults(base.driver, base.wait)  # Initializing Search Results Page class

link = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0"

# Step1. Open eBay watch page
base.open_url(link)  # Opening the link

# Step2. Select option Brand / Rolex in Filter panel
brand = "rolex"  # Defining the brand to select
left_filter_panel.select_brand(brand)  # Selecting the brand on filter panel

# Step3. Verify the first two result items contain “rolex” in their title
items_to_check = [1, 2]  # numbers as you SEE them on the page
for item in items_to_check:
    search_results.verify_item_title_contains(item, brand)

# Step4. Store title and price of the first two results in a variable
search_results_data = {"item1 - title": search_results.get_title_text(items_to_check[0]),
                       "item1 - price": search_results.get_price(items_to_check[0]),
                       "item2 - title": search_results.get_title_text(items_to_check[1]),
                       "item2 - price": search_results.get_price(items_to_check[1])
                       }

# Step5. Open item in and verify the title and the price by comparing them with the stored data
# Opening item #1 and storing the data
search_results.open_item_in_new_tab(items_to_check[0])
item_pages_data = {"item1 - title": item_page.get_title_text(),
                   "item1 - price": item_page.get_price()
                   }
base.close_tab()
# Opening item #2 and storing the data
search_results.open_item_in_new_tab(items_to_check[1])
item_pages_data.update({"item2 - title": item_page.get_title_text(),
                        "item2 - price": item_page.get_price()
                        })
base.close_tab()
# Comparing the title and the price with stored data
verification.compare_data(search_results_data, item_pages_data)

# Step6. Uncheck “Rolex“ option
left_filter_panel.deselect_brand(brand)

# Step7. Check “Casio“ option
brand = "casio"  # Defining the brand to select
left_filter_panel.select_brand(brand)  # Selecting the brand on filter panel

# Step8. Verify the last two result items contain “Casio“ in their title
items_to_check = [-1, -2]
for item in items_to_check:
    search_results.verify_item_title_contains(item, brand)

# Step9. Save and print all the mismatches if any
verification.verification_report()

# Closing the browser
base.close_browser()
