import time
import random
from rich.console  import Console
from rich.panel    import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text     import Text
from config import MODEL_CONFIG, RESULT_POOL
from engine import compute_relevance_score

console = Console()

PIPELINE_STEPS = [
    "Tokenizing query",
    "Computing semantic embedding",
    "Querying recommendation index",
    "Applying engagement signal weights",
    "Re-ranking with MMR algorithm",
    "Filtering low-quality content",
    "Resolving CDN endpoints",
]


def show_banner():
    banner = Text("Sherlock — YouTube Recommendation Engine", style="bold cyan")
    sub    = Text(
        f"Model: {MODEL_CONFIG['version']}  |  Region: {MODEL_CONFIG['region']}",
        style="dim"
    )
    console.print(Panel.fit(f"{banner}\n{sub}", border_style="cyan"))
    console.print()


def show_processing(query: str):
    console.print(f"[dim]› Query received:[/dim] [bold]{query}[/bold]\n")
    time.sleep(0.3)

    with Progress(
        SpinnerColumn(spinner_name="dots"),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        for step in PIPELINE_STEPS:
            task = progress.add_task(f"[cyan]{step}...", total=None)
            time.sleep(random.uniform(0.4, 1.1))
            progress.update(task, description=f"[green]✓ {step}")
            time.sleep(0.15)

    console.print()


def show_results(query: str, count: int):
    score = compute_relevance_score(query)
    console.print(Panel(
        f"[bold green]Found {count} videos matching your query[/bold green]\n\n"
        f"[dim]Relevance score :[/dim]  [yellow]{score}[/yellow]\n"
        f"[dim]Top result rank :[/dim]  [yellow]#1 of {count}[/yellow]\n"
        f"[dim]Quality filter  :[/dim]  [yellow]passed[/yellow]",
        title="[bold white]Results[/bold white]",
        border_style="green",
    ))
    console.print()


def prompt_user() -> str:
    return console.input(
        "[bold]Wanna play the top rated one? [Y/n]: [/bold]"
    ).strip().lower()
