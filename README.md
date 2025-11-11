# calccli

calccli is a tiny command-line calculator implemented with Typer and Rich.

It provides subcommands: `add`, `sub`, `mul`, `div`, and a `--version` flag.

Requirements
------------
- Python 3.8+

Install (for anyone)
--------------------

Option A) Install directly from GitHub (pip):

```powershell
pip install git+https://github.com/thulasiramk-2310/calccli.git
```

Option B) Install as an isolated CLI (pipx, recommended for end users):

```powershell
python -m pip install --user pipx
python -m pipx ensurepath
pipx install git+https://github.com/thulasiramk-2310/calccli.git
```

Option C) Clone and install in a virtual environment (editable for contributors):

```powershell
git clone https://github.com/thulasiramk-2310/calccli.git
cd calccli
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

Run
---

After installing (via pip or pipx):

```powershell
calccli --version
calccli add 5 10    # -> 15
calccli sub 8 3     # -> 5
calccli mul 4 2.5   # -> 10
calccli div 10 2    # -> 5
```

Run from source without installing (from project root):

```powershell
python -m calccli.main --version
python -m calccli.main add 2 3
```

Uninstall
---------
- If installed with pip: `pip uninstall calccli`
- If installed with pipx: `pipx uninstall calccli`

Notes
-----
- Division by zero is handled gracefully (prints an error and exits with code 1).
- Output is colorized using Rich.

