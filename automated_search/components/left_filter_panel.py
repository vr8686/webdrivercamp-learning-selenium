from automated_search.components.base import Base
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class LeftFilterPanel(Base):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def select_brand(self, brand):
        brand_selection_locator = (By.XPATH, f'//span[@class="cbx x-refine__multi-select-cbx" and '
                                             f'contains(translate(text(),"ABCDEFGHIJKLMNOPQRSTUVWXYZ",'
                                             f'"abcdefghijklmnopqrstuvwxyz"), "{brand.lower()}")]')
        print(f'Selecting brand: "{brand}"')
        self.click_element(brand_selection_locator)
        if self.wait.until(ec.visibility_of_element_located(brand_selection_locator)):
            print(f"Filter by Brand/{brand} applied. "
                  f"Current url is: {self.driver.current_url}")

    def deselect_brand(self, brand):
        brand_selection_locator = (By.XPATH, f'//span[@class="cbx x-refine__multi-select-cbx" and '
                                             f'contains(translate(text(),"ABCDEFGHIJKLMNOPQRSTUVWXYZ",'
                                             f'"abcdefghijklmnopqrstuvwxyz"),'
                                             f'"{brand.lower()}")]')
        print(f'Removing brand: "{brand}" selection')
        self.click_element(brand_selection_locator)
        if self.wait.until(ec.visibility_of_element_located(brand_selection_locator)):
            print(f"Filter by Brand/{brand} removed. "
                  f"Current url is: {self.driver.current_url}")
