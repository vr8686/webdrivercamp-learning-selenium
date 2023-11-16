from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class Base:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_url(self, url):
        self.driver.get(url)
        print(f"Opening page... Current url is: {self.driver.current_url}")

    def click_element(self, locator):
        if not self.wait.until(ec.element_to_be_clickable(locator)):
            print(f"Error. Element located by {locator} is NOT clickable")
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        text = self.wait.until(ec.visibility_of_element_located((By.XPATH, locator))).text
        return text

    def extract_float_price(self, text):
        valid_chars = set("0123456789.")
        num_chars = []
        decimal_point_seen = False
        for char in text:
            if char in valid_chars:
                if char == '.':
                    if not decimal_point_seen:
                        num_chars.append(char)
                        decimal_point_seen = True
                else:
                    num_chars.append(char)

        num_str = ''.join(num_chars)
        result = float(num_str)
        return result

    def switch_webdriver_to_the_new_tab(self):
        new_tab_handle = self.driver.window_handles[-1]  # Assuming the new tab is the last one opened
        self.driver.switch_to.window(new_tab_handle)

    def close_tab(self):
        print("Closing current tab...")
        self.driver.close()
        initial_tab_handle = self.driver.window_handles[0]  # Assuming the initial tab is the first one opened
        self.driver.switch_to.window(initial_tab_handle)
        print(f"Current url is: {self.driver.current_url}")

    def close_browser(self):
        self.driver.quit()
