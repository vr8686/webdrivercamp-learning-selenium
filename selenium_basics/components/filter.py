from .base import Base

class LeftFilter(Base):
    LOCATOR = "//"

    def __init__(self, driver):
        super().__init__(driver)

    def select_option(self, option, visible=False):
        print(Base.BASE_VAR)
        print(LeftFilter.LOCATOR)
        print(option)
        print(visible)