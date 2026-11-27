"""The Product class. It uses the helper functions from the same package."""
from shop.helpers import add_vat, format_sek


class Product:
    def __init__(self, name, unit_price):
        self.name = name
        self.unit_price = unit_price

    def price_with_vat(self):
        return add_vat(self.unit_price)

    def describe(self):
        return f"{self.name}: {format_sek(self.price_with_vat())} incl. VAT"
