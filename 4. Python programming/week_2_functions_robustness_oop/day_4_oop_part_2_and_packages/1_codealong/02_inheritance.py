"""Topic 2: Inheritance (light)

Idea: a child class gets everything from its parent class, and only changes what is different.
Use it only when the child IS A kind of the parent: a digital product IS A product.

Run this file with the ▶ button, or in the terminal: python 02_inheritance.py
"""


class Product:
    def __init__(self, name, unit_price):
        self.name = name
        self.unit_price = unit_price

    def shipping_cost(self):
        return 49

    def total_price(self):
        return self.unit_price + self.shipping_cost()

    def describe(self):
        return f"{self.name}: {self.unit_price} SEK + {self.shipping_cost()} SEK shipping = {self.total_price()} SEK"


class DigitalProduct(Product):              # DigitalProduct IS A Product
    def shipping_cost(self):                # override: there is nothing to ship
        return 0


def main():
    book = Product("Paper book", 199)
    ebook = DigitalProduct("E-book", 99)

    print(book.describe())
    print(ebook.describe())

    # DigitalProduct got __init__, total_price() and describe() from Product for free.
    # It only changed shipping_cost(). describe() automatically uses the right version.

    # The same code works for both kinds of product
    basket = [book, ebook, Product("Mouse", 299)]
    total = 0
    for item in basket:
        total = total + item.total_price()
    print("Basket total:", total, "SEK")


# -----------------------------------------------------------------------------
# Your turn
# -----------------------------------------------------------------------------
# 1. Create a class HeavyProduct(Product) with a shipping cost of 149 SEK.
# 2. In main(): add a heavy product (for example a desk, 2490 SEK) to the basket
#    and print the new total.

main()
