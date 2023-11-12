from automated_search.components.base import Base


class ItemPage(Base):
    ITEM_TITLE_LOCATOR = '//h1//span[@class="ux-textspans ux-textspans--BOLD"]'
    ITEM_PRICE_LOCATOR = '//div[@id="mainContent"]//*[@class="x-price-primary"]/span[@class="ux-textspans"]'

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def get_title_text(self) -> str:
        title_text = self.get_text(ItemPage.ITEM_TITLE_LOCATOR)
        print(f'Item title is: {title_text}')
        return title_text

    def get_price(self) -> float:
        text = self.get_text(ItemPage.ITEM_PRICE_LOCATOR)
        price = self.extract_float_price(text)
        print(f'Item price is: {price}')
        return price
