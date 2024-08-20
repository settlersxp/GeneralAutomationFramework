from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import dataBroker as Data
from Frontend.Components.base import Base
from Utils.USelectorTypes import USelectorTypes
from Utils.USelectors import USelectors


class Selectors(USelectors):
    a_title = USelectorTypes(selector="strong.product-item-name")
    a_image = USelectorTypes(selector="img.product-image-photo")
    a_price = USelectorTypes(selector='[data-price-type="finalPrice"]')

    # an example on how to select a swatch without making it a component
    swatch = USelectorTypes(selector='//div[starts-with(@class,"swatch-opt")]', by=By.XPATH, is_list=True)
    swatch_size = USelectorTypes(selector='//div[starts-with(@id,"option-label-size-")]', by=By.XPATH, is_list=True)
    swatch_color = USelectorTypes(selector='//div[starts-with(@id,"option-label-color-")]', by=By.XPATH, is_list=True)
    add_to_cart = USelectorTypes(selector='button.action.tocart.primary')


class ProductItem(Base):
    def __init__(self):
        super().__init__(relative=True)
        self.name = "Product item"
        self.selectors = Selectors()
        self.on_load()

    def add_to_cart(self):
        if self.selectors.swatch_size.count() > 0:
            self.selectors.swatch_size.get().click()

        if self.selectors.swatch_color.count() > 0:
            self.selectors.swatch_color.get().click()

        ActionChains(Data.BROWSER) \
            .move_to_element(self.selectors.swatch.get()) \
            .move_to_element(self.selectors.add_to_cart.get()) \
            .perform()
