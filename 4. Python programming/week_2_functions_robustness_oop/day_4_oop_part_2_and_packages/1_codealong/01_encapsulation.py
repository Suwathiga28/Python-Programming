"""Topic 1: Encapsulation

Idea: an object looks after its own data, so nobody can put it in a nonsense state.

How this file is organised (we do the same in every file we run):
1. first the DEFINITIONS (classes and functions)
2. then a function main() with the code that should run
3. on the very last line we call main()

Run this file with the ▶ button, or in the terminal: python 01_encapsulation.py
"""


# -----------------------------------------------------------------------------
# The problem: anyone can change an attribute to anything
# -----------------------------------------------------------------------------
class OpenProduct:
    def __init__(self, name, unit_price):
        self.name = name
        self.unit_price = unit_price


# -----------------------------------------------------------------------------
# The solution: keep the data "inside" and change it through methods.
# A leading underscore (_unit_price) means: internal, please use the methods.
# -----------------------------------------------------------------------------
class Product:
    def __init__(self, name, unit_price):
        self.name = name
        self.set_price(unit_price)          # validate already when the object is created

    def get_price(self):
        return self._unit_price

    def set_price(self, value):
        if value < 0:
            raise ValueError(f"price cannot be negative, got {value}")
        self._unit_price = value

    def describe(self):
        return f"{self.name}: {self._unit_price:.2f} SEK"


def main():
    # 1. Nothing stops bad data in OpenProduct
    mouse = OpenProduct("Mouse", 299)
    mouse.unit_price = -50
    print("Open product, price:", mouse.unit_price)

    # 2. Product looks after its own price
    laptop = Product("Laptop", 9990)
    print(laptop.describe())

    laptop.set_price(8990)
    print("New price:", laptop.get_price())

    # 3. Bad data is stopped (day 2: raise and try/except)
    try:
        laptop.set_price(-5)
    except ValueError as e:
        print("Not allowed:", e)

    try:
        broken = Product("Broken", -1)
    except ValueError as e:
        print("Not allowed:", e)

    print("Price is still:", laptop.get_price())

    # Python does not *enforce* the underscore: laptop._unit_price = -5 would work.
    # The underscore is a promise between programmers: "do not touch this directly".


# -----------------------------------------------------------------------------
# Your turn
# -----------------------------------------------------------------------------
# 1. Add a method apply_discount(percent) to Product. Use set_price() inside it,
#    so the price can never become negative.
# 2. In main(): what happens with laptop.apply_discount(150)? Catch the error and print it.

main()
