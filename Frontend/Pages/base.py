import dataBroker as Data


class Base:
    def __init__(self):
        super().__init__()
        self.name = None
        self.url = None

    def open_page(self):
        Data.BROWSER.get(self.url)
