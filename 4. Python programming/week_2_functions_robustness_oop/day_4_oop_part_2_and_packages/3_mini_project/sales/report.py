"""SalesReport: load a sales file, keep the valid rows and summarise them."""
import csv
import json

from sales.parsing import parse_row


def get_revenue(item):
    """Helper for sorting: returns the revenue of one {"customer": ..., "revenue": ...} dict."""
    return item["revenue"]


class SalesReport:
    def __init__(self, path):
        # TODO: store the path, and create two empty lists: self.rows and self.errors
        pass

    def load(self):
        """Read the CSV file.

        - every valid row becomes a SaleRow in self.rows (use parse_row)
        - an invalid row must NOT crash the program: add a dict
          {"order_id": ..., "error": "..."} to self.errors instead
        - if the file does not exist, raise FileNotFoundError with a clear message
        """
        # TODO
        pass

    def total_revenue(self):
        """Return the total revenue of all valid rows (use a loop)."""
        # TODO
        pass

    def revenue_by_category(self):
        """Return a dict {category: revenue}."""
        # TODO
        pass

    def revenue_by_customer(self):
        """Return a dict {customer: revenue}."""
        # TODO
        pass

    def top_customers(self, n=3):
        """Return the n best customers as a list of dicts {"customer": ..., "revenue": ...}, highest revenue first.

        Hint: build the list from revenue_by_customer(), then sort it with
        sorted(the_list, key=get_revenue, reverse=True)
        """
        # TODO
        pass

    def describe(self):
        """Return a text of several lines: the file, the number of valid and invalid rows,
        the total revenue and the top customers."""
        # TODO
        pass

    def to_json(self, path):
        """Save valid_rows, invalid_rows, total_revenue, revenue_by_category,
        top_customers and errors to a JSON file."""
        # TODO
        pass
