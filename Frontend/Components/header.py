import dataBroker as Data
from Frontend.Components.base import Base
from Utils.USelectorTypes import USelectorTypes
from Utils.USelectors import USelectors


class Selectors(USelectors):
    a_wrapper = USelectorTypes(selector="header.page-header")
    # this is a more complex CSS selector which takes into account the SEO attribute
    a_logo = USelectorTypes(selector="a.logo[aria-label='store logo']")
    a_search_input = USelectorTypes(selector="input#search")
    a_search_button = USelectorTypes(selector="button.search")

    cart_items = USelectorTypes(selector='span.counter-number')


class Header(Base):
    def __init__(self):
        super().__init__()
        self.name = "Header"
        self.selectors = Selectors()
        self.on_load()

    # example interaction with the elements of the component
    def search(self, query):
        Data.BROWSER.input_text(self.selectors.a_search_input, query)
        Data.BROWSER.click(self.selectors.a_search_button)
