from automated_search.components.base import Base
from automated_search.components import verification
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class LeftFilterPanel(Base):
    LOCATOR = (By.XPATH, '//ul[@class="x-refine__body x-refine__body--flush-left x-refine__body--has-toggle"]')

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def select_brand(self, brand):
        brand_selection_locator = (By.XPATH, f'//span[@class="cbx x-refine__multi-select-cbx" and contains(translate(text(),"ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz"), "{brand.lower()}")]')
        print(f'Selecting brand: "{brand}"')
        self.click_element(brand_selection_locator)
        if self.wait.until(ec.visibility_of_element_located(LeftFilterPanel.LOCATOR)):
            print(f"Filter by Brand/{brand} applied. "
                  f"Current url is: {self.driver.current_url}")

    def deselect_brand(self, brand):
        brand_selection_locator = (By.XPATH, f'//span[@class="cbx x-refine__multi-select-cbx" and '
                                             f'contains(translate(text(),"ABCDEFGHIJKLMNOPQRSTUVWXYZ",'
                                             f'"abcdefghijklmnopqrstuvwxyz"),'
                                             f'"{brand.lower()}")]')
        print(f'Removing brand: "{brand}" selection')
        self.click_element(brand_selection_locator)
        if self.wait.until(ec.visibility_of_element_located(LeftFilterPanel.LOCATOR)):
            print(f"Filter by Brand/{brand} removed. "
                  f"Current url is: {self.driver.current_url}")


class SearchResults(Base):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    @classmethod
    def real_item_number(cls, item: int):
        real_number = 0
        if 1 <= item <= 8:
            real_number = item + 1
        elif 9 <= item <= 60:
            real_number = item + 2
        elif -52 <= item <= -1:
            real_number = 63 - abs(item)
        elif -60 <= item <= -53:
            real_number = 62 - abs(item)
        return real_number

    @classmethod
    def item_title_locator(cls, item_number):
        real_item_number = SearchResults.real_item_number(item_number)
        item_title_locator = f'//li[@data-gr4="{real_item_number}"]//span[@role="heading"]'
        return item_title_locator

    def open_item_in_new_tab(self, item_number: int):
        real_item_number = SearchResults.real_item_number(item_number)
        item_locator = (By.XPATH, f'//li[@data-gr4="{real_item_number}"]//span[@role="heading"]')
        # item_locator = (By.XPATH, SearchResults.item_title_locator(item_number))
        print(f'Opening item #{item_number} in the new tab...')
        self.click_element(item_locator)
        print(f"Opening page... Current url is: {self.driver.current_url}")
        self.switch_webdriver_to_the_new_tab()

    def verify_item_title_contains(self, item_number: int, keyword: str):
        print(f'Checking if title of item #{item_number} contains word \"{keyword}\"...')
        title_text = SearchResults.get_title_text(self, item_number)
        if keyword in title_text.lower():
            print(f'Success. The title of item #{item_number} contains \"{keyword}\".')
        else:
            mismatch = f'Mismatch. The title of item #{item_number} DOES NOT contain \"{keyword}\"'
            print(mismatch)
            verification.MISMATCHES.append(mismatch)

    def get_title_text(self, item_number) -> str:
        real_item_number = SearchResults.real_item_number(item_number)
        item_title_locator = f'//li[@data-gr4="{real_item_number}"]//span[@role="heading"]'
        title_text = self.get_text(item_title_locator)
        print(f'Item #{item_number} title is: {title_text}')
        return title_text

    def get_price(self, item_number) -> float:
        real_item_number = SearchResults.real_item_number(item_number)
        item_price_locator = f'//li[@data-gr4="{real_item_number}"]//span[@class="s-item__price"]'
        text = self.get_text(item_price_locator)
        price = self.extract_float_price(text)
        print(f'Item #{item_number} price is: {price}')
        return price
