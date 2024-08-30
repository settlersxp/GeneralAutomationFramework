import dataBroker as Data
from Frontend.Components.base import Base
from Utils.USelectorTypes import USelectorTypes
from Utils.USelectors import USelectors


class Rules():
    def user_status(self, authenticated_user, anonymous_user):
        # this rule can be as complex as needed but make sure to return a selector
        if Data.LOGGED_USER:
            return authenticated_user
        else:
            return anonymous_user


class Selectors(USelectors):
    def __init__(self):
        rules = Rules()
        a_wrapper = USelectorTypes(selector="header.page-header")
        # this is a more complex CSS selector which takes into account the SEO attribute
        self.a_logo = USelectorTypes(selector="a.logo[aria-label='store logo']")
        self.a_search_input = USelectorTypes(selector="input#search")
        self.a_search_button = USelectorTypes(selector="button.search")

        self.cart_items = USelectorTypes(selector='span.counter-number')

        # they are not prefixed with "a_" because we don't know which one to load but we let them here to be grouped
        # with the other selectors
        self.authenticated_user = USelectorTypes(selector="a.user_name")
        self.anonymous_user = USelectorTypes(selector="")
        # but the user is prefixed with "a_" because after resolving the rule we know which one to load
        self.a_user = rules.user_status(
            authenticated_user=self.authenticated_user,
            anonymous_user=self.anonymous_user
        )


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
