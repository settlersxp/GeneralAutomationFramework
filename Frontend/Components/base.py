import dataBroker as Data
from Utils.USelectors import USelectors


class Base:
    def __init__(self, relative=False):
        super().__init__()
        self.name = None
        # if the component is relative to another component set this flag to true.
        # Relative components do not reset the scope of the browser to the root element
        self.relative = relative
        self.selectors: USelectors = USelectors()

    def on_load(self):
        # wait for the page to load
        Data.BROWSER.wait_for_page_load()

        if not self.relative:
            Data.BROWSER = Data.BROWSER.find_element("html")

        for name, selector in self.selectors.__dict__.items():
            if name.startswith("a_"):
                # validate that the selector exists on the page and crash automatically if it doesn't
                selector.get()

        if not self.relative:
            # change the focus of the browser to the current component so that the selectors are
            # used in the correct context. For relative components, the focus is not changed because is preset
            # by the parent component
            Data.BROWSER = self.selectors.a_wrapper.get()
