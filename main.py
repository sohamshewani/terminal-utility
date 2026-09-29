import typer
from rich.console import Console
from rich.table import Table
import sympy as sp
import psutil

app = typer.Typer(help="Terminal Personal Swiss Army Knife")
console = Console()

@app.command()
def math(expression: str):
    """Solve or simplify symbolic math expressions instantly."""
    try:
        x = sp.Symbol('x')
        parsed = sp.sympify(expression)
        solution = sp.solve(parsed, x)
        console.print(f"[bold green]Expression:[/bold green] {parsed}")
        console.print(f"[bold cyan]Solutions (for x):[/bold cyan] {solution}")
    except Exception as e:
        console.print(f"[bold red]Error parsing math:[/bold red] {e}")

@app.command()
def stats():
    """Display quick Apple Silicon resource telemetry."""
    table = Table(title="System Telemetry")
    table.add_column("Resource", style="magenta")
    table.add_column("Usage", style="green")

    ram = psutil.virtual_memory()
    table.add_row("CPU Load", f"{psutil.cpu_percent()}%")
    table.add_row("Memory Used", f"{ram.percent}% ({round(ram.used / (1024**3), 1)} GB / {round(ram.total / (1024**3), 1)} GB)")
    console.print(table)

if __name__ == "__main__":
    app()
