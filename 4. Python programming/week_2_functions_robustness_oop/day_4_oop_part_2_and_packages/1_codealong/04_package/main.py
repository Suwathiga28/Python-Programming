"""Topic 4: A package = a folder of .py files that belong together

    04_package/
    ├── main.py            <- the file you run
    └── shop/              <- the package
        ├── __init__.py    <- empty, marks "shop" as a package
        ├── helpers.py     <- price functions
        └── products.py    <- the Product class (imports from shop.helpers)

To import from a package write:   from package.module import name

Rule of thumb: files inside the package only DEFINE functions and classes.
The file you run (main.py) puts its code in a function main() and calls main() on the last line.

Run this file with the ▶ button, or in the terminal (from this folder): python main.py
"""
from shop.helpers import format_sek
from shop.products import Product


def main():
    products = [Product("Laptop", 9990), Product("Mouse", 299), Product("Notebook", 25)]

    total = 0
    for product in products:
        print(product.describe())
        total = total + product.price_with_vat()

    print("Total:", format_sek(total))


# Try it:
# 1. Add a new module shop/discounts.py with a function ten_percent_off(price).
# 2. Import it here and print the total after the discount.

main()
