# Python programming

Course material for **Python for Data Analysts**: code-alongs, labs and data for every week and day.

Start with the **course guide**: [`00_course_info/Python_Course_Guide.pdf`](00_course_info/Python_Course_Guide.pdf). It has one block per day with the goals, the key ideas, the files we use, and the homework.

## Get the material

- **With Git:** `git clone https://github.com/HI-python-programming/python-programming.git`, and later `git pull` to get new material.
- **Without Git:** click the green **Code** button on GitHub, then **Download ZIP**.

> **Tip:** to do a lab, make a copy of the notebook with your name in it (for example `02_lab_lists_anna.ipynb`). New files never get in the way of `git pull`.

## Setup (once)

1. Install **Python 3.13** from [python.org](https://www.python.org/downloads/). On Windows, tick **"Add python.exe to PATH"**.
2. Install **VS Code** and the extensions **Python** and **Jupyter** (VS Code suggests them when you open this folder).
3. Open this folder in VS Code: *File > Open Folder*.
4. Open a terminal (*View > Terminal*) and run:

   ```
   python -m venv .venv
   .venv\Scripts\Activate.ps1          (Windows PowerShell)
   source .venv/bin/activate           (Mac)
   pip install -r requirements.txt
   ```

5. Open a notebook (`.ipynb`), click **Select Kernel** (top right) and choose `.venv`.

Problems? See *Getting started* in the course guide.

## What is where

| Folder | Content |
|---|---|
| `00_course_info/` | The course guide and a handout on Python terms |
| `week_1_bootcamp/` | Variables, strings, lists, conditionals, loops, dictionaries (3 days) |
| `week_2_functions_robustness_oop/` | Functions, errors, files, classes, `.py` files and packages (4 days) |
| `week_3_pandas_1/` | pandas: DataFrames, selecting, filtering, a first chart |
| `week_4_pandas_2_cleaning/` | Cleaning data |
| `week_5_pandas_3_and_apis/` | Grouping, pivot tables, merging; getting data from APIs |
| `week_6_plotly/` | Visualisation with Plotly |

Material for weeks 7 to 9 is added later.

Every week has a folder and every day a subfolder. Inside, files are numbered in the order we use them:

- `01_codealong_...`: we go through it together
- `02_lab_...`: you practise on your own (labs are individual work)
- `bonus_...` and `..._HOMEWORK`: extra practice at home

Data files (`.csv`) are next to the notebook that uses them. Solutions are shared after the labs.
