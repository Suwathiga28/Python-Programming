"""The SaleRow class: one valid row of sales data."""


class SaleRow:
    def __init__(self, order_id, date, customer, product, category, quantity, unit_price):
        # TODO: store every argument as an attribute, for example  self.order_id = order_id
        pass

    def revenue(self):
        # TODO: return quantity * unit_price
        pass

    def describe(self):
        # TODO: return a short text, for example "Order 1001 (Anna): Laptop x 1 = 9990.00 SEK"
        pass
