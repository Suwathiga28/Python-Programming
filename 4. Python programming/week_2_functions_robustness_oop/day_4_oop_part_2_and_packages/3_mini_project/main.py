"""Run the sales report.

Run this file with the ▶ button, or in the terminal (from this folder): python main.py
"""
from pathlib import Path

# TODO: import the class SalesReport from the module report in the package sales
#       (look at how check_my_work.py imports it)


def main():
    report = SalesReport("data/sales_raw.csv")
    try:
        report.load()
    except FileNotFoundError as e:
        print(e)
        print("Tip: run this file from the 3_mini_project folder (cd into it first).")
        return

    print(report.describe())
    print()
    print("Rows that could not be used:")
    for error in report.errors:
        print(f"  order {error['order_id']}: {error['error']}")

    Path("output").mkdir(exist_ok=True)
    report.to_json("output/report.json")
    print()
    print("Saved output/report.json")


main()
