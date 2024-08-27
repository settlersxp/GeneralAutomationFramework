import unittest


class BuyProductsTest(unittest.TestCase):
    def test_buy_product_from_homepage(self):
        from Frontend.Pages.homepage import Homepage
        homepage = Homepage()
        homepage.open_page()
        homepage.hot_sellers.focus_any_item()
        homepage.hot_sellers.add_to_cart()

        # change the focus from hot sellers to the header and validate automatically the mandatory elements
        homepage.header.on_load()
        self.assertTrue(homepage.header.selectors.cart_items().text == '1')
        homepage.header.selectors.cart_items().click()