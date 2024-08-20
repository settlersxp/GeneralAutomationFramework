from selenium.webdriver.common.by import By

import dataBroker as Data


class USelectorTypes:
    def __init__(self,
                 selector,
                 by: By = By.CSS_SELECTOR,
                 index=-1,
                 is_list=False,
                 ):
        self.selector = selector
        self.by = by
        self.index = index
        self.is_list = is_list

    def get(self):
        if self.is_list and self.index == -1:
            return Data.BROWSER.find_elements(self.by, self.selector)

        if self.index:
            return Data.BROWSER.find_elements(self.by, self.selector)[self.index]

        return Data.BROWSER.find_element(self.by, self.selector)

    def count(self):
        return len(Data.BROWSER.find_elements(self.by, self.selector))
