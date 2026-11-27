# Day 4: OOP part 2 and working with `.py` files

Today there are **no notebooks**. Real projects are made of plain Python files (`.py`) that import each other, and you run them from VS Code. This is also how the pipeline project in week 9 is built.

## Order of the day
1. **`1_codealong/`** (teacher live-codes, you follow), one file or folder per topic:
   - `01_encapsulation.py`
   - `02_inheritance.py`
   - `03_importing/`: `main.py` imports another file, `helpers.py`
   - `04_package/`: `main.py` imports from a package (a folder of `.py` files)
2. **`2_exercise_importing/`**: individual, about 30 minutes
3. **`3_mini_project/`**: individual, the rest of the day

## How our `.py` files are organised
- **Modules** (files that other files import, such as `helpers.py` or the files in a package) only **define** functions and classes. They do not run anything by themselves.
- A **file you run** (such as `main.py`) is organised in three parts:
  1. imports at the top
  2. definitions, and a function `main()` with the code that should run
  3. `main()` called on the very last line

This keeps every file tidy: you always know where the program starts.

## How to run a `.py` file in VS Code
**Option A: the ▶ button.** Open the file and click ▶ (*Run Python File*) in the top right corner. The output appears in the terminal at the bottom of the window.

**Option B: the terminal.** This works everywhere, also outside this course.
1. Open the terminal: menu *View > Terminal*.
2. Go to the folder of the file with `cd`, for example:
   ```
   cd week_2_functions_robustness_oop/day_4_oop_part_2_and_packages/3_mini_project
   ```
3. Run the file: `python main.py` (on some computers `py main.py` or `python3 main.py`).

Useful terminal commands: `cd name_of_folder` (go into a folder), `cd ..` (go up one level), `ls` or `dir` (list the files).

> The course folder contains a VS Code setting (`.vscode/settings.json`) that makes the ▶ button run a file **from its own folder**. That matters for programs that read data, such as `data/sales_raw.csv`. If you open another folder in VS Code you do not have that setting: then use option B.

## Common errors

| Error | What it usually means |
|---|---|
| `ModuleNotFoundError: No module named 'helpers'` | The file name is misspelled, or the two files are not in the same folder |
| `ModuleNotFoundError: No module named 'sales'` | The file you run is not next to the `sales/` folder |
| `ImportError: cannot import name 'add_vat'` | The file exists, but the function name is misspelled or not in that file |
| `FileNotFoundError: ... data/sales_raw.csv` | You run the program from another folder: `cd` into the project folder first |

**Never give your own file the name of a library** (`math.py`, `random.py`, `csv.py`, `json.py`, `pandas.py`). Python would import your file instead of the real library.

## Things you will see online (not needed in this course)

### Dataclasses
Many classes only hold data. Python has a shortcut that writes `__init__` for you:

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    category: str
    unit_price: float
```

The line starting with `@` is called a **decorator**: it adds extra behaviour to the class. You will meet dataclasses and decorators in code online. In this course we write `__init__` ourselves, so that we always see what happens.
