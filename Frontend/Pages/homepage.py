from Frontend.Components.hotSellers import HotSellers
from Frontend.Components.header import Header
from Frontend.Pages.base import Base
import dataBroker as Data


class Homepage(Base):
    def __init__(self):
        super().__init__()
        self.url = Data.ROOT
        self.title = "Home Page"

        # load the components that should be present on the page for automatic validation
        self.header = Header()
        self.hot_sellers = HotSellers()

        # - why not adding the cart popups here?
        # because it does not exist at the creation of the new instance of the Homepage





