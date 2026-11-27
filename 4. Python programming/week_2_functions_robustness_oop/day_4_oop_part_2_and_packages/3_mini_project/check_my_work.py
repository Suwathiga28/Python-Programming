"""Checks your mini project. Do not change this file.

Run it with the ▶ button, or in the terminal (from this folder): python check_my_work.py
Every check prints PASSED, FAILED (with a hint) or ERROR. Fix one thing at a time.
"""
import json
from pathlib import Path

from sales.models import SaleRow
from sales.parsing import parse_row
from sales.report import SalesReport

GOOD_ROW = {
    "order_id": "1",
    "date": "2025-02-01",
    "customer": "Anna",
    "product": "Pen",
    "category": "Stationery",
    "quantity": "2",
    "unit_price": "10.5",
}


def check_sale_row():
    row = SaleRow(1, "2025-02-01", "Anna", "Pen", "Stationery", 2, 10.5)
    assert row.customer == "Anna", "SaleRow should store every argument as an attribute, e.g. self.customer"
    assert row.revenue() == 21.0, "revenue() should return quantity * unit_price"
    assert "Anna" in row.describe(), "describe() should return a text that includes the customer"


def check_parse_row():
    row = parse_row(GOOD_ROW)
    assert row.quantity == 2, "quantity should be converted to an int"
    assert row.unit_price == 10.5, "unit_price should be converted to a float"
    assert row.order_id == 1, "order_id should be converted to an int"
    assert row.date.year == 2025, "date should be converted with datetime.strptime(...).date()"

    bad_values = [
        {"field": "quantity", "value": "0"},
        {"field": "quantity", "value": "abc"},
        {"field": "unit_price", "value": "-1"},
        {"field": "customer", "value": " "},
        {"field": "date", "value": "01/02/2025"},
    ]
    for bad in bad_values:
        broken = GOOD_ROW.copy()
        broken[bad["field"]] = bad["value"]
        rejected = False
        try:
            parse_row(broken)
        except ValueError:
            rejected = True
        assert rejected, f"parse_row should raise ValueError when {bad['field']} is '{bad['value']}'"


def check_load():
    report = SalesReport("data/sales_raw.csv")
    report.load()
    assert len(report.rows) == 15, f"expected 15 valid rows, got {len(report.rows)}"
    assert len(report.errors) == 5, f"expected 5 invalid rows, got {len(report.errors)}"
    error_ids = []
    for error in report.errors:
        error_ids.append(error["order_id"])
    assert error_ids == ["1006", "1007", "1010", "1013", "1016"], f"these rows were rejected: {error_ids}"


def check_missing_file():
    raised = False
    try:
        SalesReport("data/no_such_file.csv").load()
    except FileNotFoundError:
        raised = True
    assert raised, "load() should raise FileNotFoundError when the file does not exist"


def check_numbers():
    report = SalesReport("data/sales_raw.csv")
    report.load()
    total = report.total_revenue()
    assert abs(total - 36493.5) < 0.01, f"total_revenue() should be 36493.5, got {total}"
    by_category = report.revenue_by_category()
    assert abs(by_category["Stationery"] - 486) < 0.01, f"Stationery revenue should be 486, got {by_category['Stationery']}"
    top = report.top_customers(3)
    assert len(top) == 3, "top_customers(3) should return 3 customers"
    assert top[0]["customer"] == "David", f"the best customer should be David, got {top[0]['customer']}"


def check_output():
    report = SalesReport("data/sales_raw.csv")
    report.load()
    text = report.describe()
    assert "15" in text, "describe() should mention the number of valid rows (15)"
    Path("output").mkdir(exist_ok=True)
    report.to_json("output/check_report.json")
    with open("output/check_report.json", encoding="utf-8") as f:
        data = json.load(f)
    assert data["valid_rows"] == 15 and data["invalid_rows"] == 5, "to_json() should save valid_rows and invalid_rows"
    assert len(data["errors"]) == 5, "to_json() should save the list of errors"


CHECKS = [
    {"name": "1. SaleRow class (models.py)", "function": check_sale_row},
    {"name": "2. parse_row (parsing.py)", "function": check_parse_row},
    {"name": "3. load() keeps good rows and records bad ones", "function": check_load},
    {"name": "4. load() with a missing file", "function": check_missing_file},
    {"name": "5. total, categories and top customers", "function": check_numbers},
    {"name": "6. describe() and to_json()", "function": check_output},
]

def main():
    passed = 0
    for check in CHECKS:
        try:
            check["function"]()
            print(f"PASSED  {check['name']}")
            passed = passed + 1
        except AssertionError as e:
            print(f"FAILED  {check['name']}: {e}")
        except Exception as e:
            print(f"ERROR   {check['name']}: {type(e)} {e}")

    print()
    print(f"{passed} of {len(CHECKS)} checks passed")
    if passed == len(CHECKS):
        print("Well done! Now run main.py and write your reflection.")


main()
