'''
Example 95: Cart Page Object & Tests

'''

class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")
        self.remove_buttons = page.locator("button[data-test^='remove']")
        self.cart_item_names = page.locator(".inventory_item_name")
        self.cart_item_prices = page.locator(".inventory_item_price")
        
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/cart.html")
        
    def get_cart_item_count(self):
        return self.cart_items.count()
        
    def get_cart_item_names(self):
        return self.cart_item_names.all_inner_texts()
        
    def remove_item(self, item_name):
        """Remove specific item from cart"""
        item_element = self.page.locator(f"text={item_name}").locator("..").locator("..")
        item_element.locator("button").click()
        
    def remove_first_item(self):
        """Remove first item from cart"""
        self.remove_buttons.first.click()
        
    def proceed_to_checkout(self):
        self.checkout_button.click()
        
    def continue_shopping(self):
        self.continue_shopping_button.click()
        
    def is_cart_empty(self):
        return self.get_cart_item_count() == 0