import random

import dataBroker as Data
from Frontend.Components.base import Base
from Frontend.Components.productItem import ProductItem
from Utils.USelectorTypes import USelectorTypes
from Utils.USelectors import USelectors


class Selectors(USelectors):
    a_wrapper = USelectorTypes(selector=".widget.block-products-list", index=0)
    a_product_items = USelectorTypes(selector="ol")

    # if the list must contain products prefix with "a_" the selector. Currently, is assumed that it can also be empty
    # when there are no products
    list_item = USelectorTypes(selector="li.product-item", is_list=True)


class HotSellers(Base):
    def __init__(self):
        super().__init__()
        self.name = "Hot sellers"
        self.selectors = Selectors()
        self.on_load()
        self.selected_product: ProductItem = None

    def focus_any_item(self):
        all_products = self.selectors.list_item.get()
        Data.BROWSER = random.choice(all_products)

        from Frontend.Components.productItem import ProductItem
        self.selected_product = ProductItem()

    def add_to_cart(self):
        self.selected_product.add_to_cart()
