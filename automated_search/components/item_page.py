from automated_search.components.base import Base


class ItemPage(Base):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def get_title_text(self) -> str:
        item_title_locator = '//h1//span[@class="ux-textspans ux-textspans--BOLD"]'
        title_text = self.get_text(item_title_locator)
        print(f'Item title is: {title_text}')
        return title_text

    def get_price(self) -> float:
        item_price_locator = '//div[@id="mainContent"]//*[@class="x-price-primary"]/span[@class="ux-textspans"]'
        text = self.get_text(item_price_locator)
        price = self.extract_float_price(text)
        print(f'Item price is: {price}')
        return price
