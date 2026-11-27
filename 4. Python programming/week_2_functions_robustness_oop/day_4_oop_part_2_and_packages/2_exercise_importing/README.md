# Exercise: import your own files

Individual work, about 30 minutes. Solutions are shared after the exercise.

## Part A: one helper file
1. In this folder, create a new file called `text_tools.py`.
2. Write two functions in it:
   - `shout(text)`: returns the text in capital letters with `!` at the end. `shout("hello")` gives `"HELLO!"`
   - `initials(full_name)`: returns the initials. `initials("Ada Lovelace")` gives `"A.L."`

   *Hint: `full_name.split()` gives a list of the words, and `word[0]` is the first letter of a word.*
3. Open `main.py` and do the TODOs: import your two functions, and remove the `#` in front of the `print` lines.
4. Run `main.py` (▶ button, or `python main.py` in the terminal).

## Part B: turn it into a package
1. Create a folder called `tools` in this folder.
2. Inside `tools`, create an empty file called `__init__.py`. It tells Python: this folder is a package.
3. Move `text_tools.py` into the `tools` folder.
4. Run `main.py` again. Which error do you get, and why?
5. Fix the import in `main.py`: `from tools.text_tools import shout, initials`
6. Run it again.

## Part C (bonus): a second module
1. Create `tools/money.py` with a function `format_sek(amount)` that returns, for example, `"1234.50 SEK"`.
2. Import it in `main.py` and print `format_sek(1234.5)`.
3. Think about it: why should you never call your own file `math.py` or `random.py`?
