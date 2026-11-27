# Mini project: the `sales` package

**Individual work, the rest of the day.**

Combine everything from week 2 in one small, well-structured program: functions, error handling, files (CSV and JSON), classes, and code split over several `.py` files.

## The task
`data/sales_raw.csv` contains 20 webshop orders. Some rows are broken on purpose. Complete the package `sales` so that `main.py` can load the file, keep the valid rows, report the invalid ones and save a summary, **without crashing on bad data**.

## The structure
```
3_mini_project/
├── main.py              runs the program (you only add one import line)
├── check_my_work.py     checks your code (do not change it)
├── data/
│   └── sales_raw.csv
└── sales/               the package you complete
    ├── __init__.py      empty: marks "sales" as a package
    ├── models.py        class SaleRow: one valid row
    ├── parsing.py       function parse_row(): one row of text -> a SaleRow
    └── report.py        class SalesReport: load, summarise, save
```

Each file has one job, and the files import each other: `report.py` imports `parse_row` from `parsing.py`, which imports `SaleRow` from `models.py`.

## How to work
1. **`sales/models.py`**: complete the class `SaleRow`.
2. **`sales/parsing.py`**: complete `parse_row(row)`. It is almost the same as `parse_row()` from the day 2 lab, but it returns a `SaleRow` object instead of a dict.
3. **`sales/report.py`**: complete `SalesReport`, one method at a time.
4. **`main.py`**: add the import line (see the TODO) and run it.

After each step, run the checks: `python check_my_work.py` (or the ▶ button). Each check prints `PASSED`, `FAILED` (with a hint) or `ERROR`. Fix one thing at a time.

When everything works, `main.py` prints something like:
```
Sales report for data/sales_raw.csv
  valid rows   : 15
  invalid rows : 5
  total revenue: 36,493.50 SEK
  top customers:
    David       11,315.50 SEK
    ...
```
and saves `output/report.json`.

## Requirements (these are the S6 distinction criteria)
- **Modularity:** small functions and methods with one job each, with docstrings; code split over modules
- **Error handling:** invalid rows are recorded, not fatal; a missing file gives a clear error
- **Structure:** a class for one row, a class for the job, a package with one module per responsibility

## Rules
- Files in `sales/` only *define* functions and classes.
- A file you run (`main.py`, `check_my_work.py`) has its imports at the top, puts its code in a function `main()`, and calls `main()` on the last line.
- Plain loops are enough: you do not need anything we have not covered.

## Reflection
Write 3 to 5 sentences in a new file `reflection.md`:
1. Which of your functions or methods is the easiest to reuse in another project? Why?
2. What would break if the file had a new column, or dates written as `DD-MM-YYYY`?
3. Why is it useful to split code over several files?

## Extensions
- Accept dates written as `DD-MM-YYYY` as well
- Add `revenue_by_month()` to `SalesReport`
- Add a module `sales/export.py` that writes the valid rows to `output/sales_clean.csv`, and use it in `main.py`
