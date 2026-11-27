"""Turn one row of the CSV file (a dict of strings) into a SaleRow."""
from datetime import datetime

from sales.models import SaleRow


def parse_row(row):
    """Return a SaleRow built from one row of csv.DictReader (a dict of strings).

    Raise ValueError with a clear message if the row is invalid:
    - the customer is empty (or only spaces)
    - quantity is not a whole number above 0
    - unit_price is not a number, or is negative
    - the date is not in the format YYYY-MM-DD

    Hint: this is almost the same as parse_row() from the day 2 lab,
    but it returns a SaleRow object instead of a dict.
    """
    # TODO
    pass
