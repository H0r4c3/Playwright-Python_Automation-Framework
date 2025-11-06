'''
Example 93: Products Page Object
What it does:

Represents the products/inventory page
Methods for adding to cart, sorting, getting product info
Reusable across multiple tests
'''
class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.product_items = page.locator(".inventory_item")
        self.add_to_cart_buttons = page.locator("button[data-test^='add-to-cart']")
        self.remove_buttons = page.locator("button[data-test^='remove']")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.product_names = page.locator(".inventory_item_name")
        self.product_prices = page.locator(".inventory_item_price")
        
    def get_product_count(self):
        return self.product_items.count()
        
    def add_product_to_cart(self, product_name):
        """Add specific product to cart by name"""
        self.page.locator(f"text={product_name}").locator("..").locator("..").locator("button").click()
        
    def add_first_product_to_cart(self):
        """Add the first product to cart"""
        self.add_to_cart_buttons.first.click()
        
    def get_cart_count(self):
        """Get number of items in cart badge"""
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0
        
    def go_to_cart(self):
        self.cart_link.click()
        
    def sort_products(self, option):
        """Sort products by option: 'az', 'za', 'lohi', 'hilo'"""
        self.sort_dropdown.select_option(option)
        
    def get_all_product_names(self):
        return self.product_names.all_inner_texts()
        
    def get_all_product_prices(self):
        prices_text = self.product_prices.all_inner_texts()
        # Convert "$29.99" to 29.99
        return [float(price.replace("$", "")) for price in prices_text]