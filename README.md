# FindTheString

This is a small Python tool that helps you **search for any text inside files with a specific extension** — recursively through folders.
You can also tell it which folders to ignore (like `node_modules` or `.git`), so it doesn’t waste time digging where you don’t want it.
![image](https://github.com/user-attachments/assets/a7c22039-fc86-4051-a5f0-1879569d3a38)

---

## What can it do?

* Search **all files** with the extension you want (e.g. `.js`, `.py`)
* Look inside those files for the text you specify
* Show you **which files and lines** contain that text
* Skip folders you don’t want to check
* Use it from the command line or import the function into your Python projects

---

## How to use it?

### From the command line (CLI)

Just run it like this:

```bash
python FindTheString.py -p "path/to/folder" -e <extension> -s <text> -i <ignored_folders>
```

Where:

* `-p` — the folder where you want to search
* `-e` — the file extension to look into (don’t forget the dot)
* `-s` — the text you want to find inside files
* `-i` — optional, a comma-separated list of folders to skip

Example:

```bash
python FindTheString.py -p "C:\Users\nolimanom\Desktop\NewFolder" -e .md -s Hello -i __pycache__,venv
```

---

### Using as a module in your Python code

If you want to use it inside your scripts, just:

```python
from FindTheString import find

folder = "C:/Users/nolimanom/Desktop/NewFolder"
extension = ".md"
search_string = "Hello"
ignore_dirs = ["__pycache__"]

results = find(folder, extension, search_string, ignore_dirs)

if not results:
    print("No matches found.")
else:
    for match in results:
        print(f"File: {match['file']}")
        print(f" Line {match['line_number']}: {match['line_content']}")
        print()

```

---

## Requirements

* Python (tested on 3.13.0)
* argparse

---

## Why?

Sometimes you just need to find that one string buried somewhere in thousands of files — this tool makes that easy, fast, and flexible.

---

## License

MIT — do whatever you want with it.

---

If you have questions or want help, just open an issue!
