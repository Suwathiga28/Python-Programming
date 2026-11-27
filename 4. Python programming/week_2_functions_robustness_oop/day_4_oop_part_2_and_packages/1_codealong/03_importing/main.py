"""Topic 3: Importing another .py file

You already import libraries: import math, import csv, import json.
Your own file works exactly the same way: helpers.py can be imported as "helpers".

Run this file with the ▶ button, or in the terminal (from this folder): python main.py
"""

# Imports always go at the top of the file.

# Way 1: import the whole file, then write  file_name.function_name
import helpers

# Way 2: import only what you need, then use the names directly
from helpers import add_vat, format_sek

# Way 3: a short nickname (you will see this with pandas:  import pandas as pd)
import helpers as h


def main():
    # Way 1
    print(helpers.format_sek(1234.5))
    print(helpers.add_vat(100))
    print("VAT rate:", helpers.VAT_RATE)

    # Way 2
    print(format_sek(add_vat(9990)))

    # Way 3
    print(h.format_sek(49))


# Try it:
# 1. Misspell the name: import helper   -> ModuleNotFoundError
#    Python looks for helper.py in the same folder as main.py (and in installed libraries).
# 2. Import a function that does not exist: from helpers import remove_vat   -> ImportError

main()
