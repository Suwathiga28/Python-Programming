"""Helper functions for prices.

This file only DEFINES things. It does not run anything by itself:
other files import it.
"""

VAT_RATE = 0.25


def add_vat(price):
    """Return the price including Swedish VAT (25%)."""
    return price * (1 + VAT_RATE)


def format_sek(amount):
    """Format a number as a price, for example 1234.5 -> '1234.50 SEK'."""
    return f"{amount:.2f} SEK"
