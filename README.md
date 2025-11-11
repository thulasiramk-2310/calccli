# calccli

calccli is a tiny command-line calculator implemented with Typer and Rich.

Usage
-----

Install locally:

```bash
pip install .
```

Run the commands:

```bash
calccli add 5 10    # -> 5 + 10 = 15
calccli sub 8 3     # -> 8 - 3 = 5
calccli mul 4 2.5   # -> 4 * 2.5 = 10
calccli div 10 2    # -> 10 / 2 = 5
calccli --version   # prints package version
```

Notes
-----

- Division by zero is handled gracefully (returns non-zero exit code and prints an error).
- The CLI prints colored output using Rich.
