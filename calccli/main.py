"""Command-line interface for calccli.

Provides basic arithmetic subcommands: add, sub, mul, div.
Uses Typer for CLI and Rich for colored output.
"""
from typing import Optional

import typer
from rich.console import Console

from calccli import __version__

app = typer.Typer(help="Simple calculator CLI")
console = Console()


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(
        None, "--version", "-v", help="Show version and exit"
    ),
):
    """Main callback. If --version is passed, print version and exit.

    When no subcommand is given, Typer will show help by default.
    """
    if version:
        console.print(f"[bold green]calccli[/] [cyan]{__version__}[/]")
        raise typer.Exit()


def _print_result(a: float, b: float, op: str, result: float) -> None:
    console.print(f"[bold]{a} {op} {b} =[/] [yellow]{result}[/]")


@app.command()
def add(a: float = typer.Argument(..., help="First number"), b: float = typer.Argument(..., help="Second number")):
    """Add two numbers."""
    _print_result(a, b, "+", a + b)


@app.command()
def sub(a: float = typer.Argument(..., help="Minuend"), b: float = typer.Argument(..., help="Subtrahend")):
    """Subtract two numbers (a - b)."""
    _print_result(a, b, "-", a - b)


@app.command()
def mul(a: float = typer.Argument(..., help="First factor"), b: float = typer.Argument(..., help="Second factor")):
    """Multiply two numbers."""
    _print_result(a, b, "*", a * b)


@app.command()
def div(a: float = typer.Argument(..., help="Dividend"), b: float = typer.Argument(..., help="Divisor")):
    """Divide two numbers. Handles divide-by-zero gracefully."""
    if b == 0:
        console.print("[bold red]Error:[/] Cannot divide by zero.")
        raise typer.Exit(code=1)
    _print_result(a, b, "/", a / b)


def run() -> None:
    """Entry point used by the console script."""
    app()


def main() -> None:
    """Compatibility wrapper named `main` so console scripts can point to calccli.main:main.

    This satisfies the requirement that the entry point run the `main()` function in
    `calccli/main.py`.
    """
    run()


if __name__ == "__main__":
    main()
