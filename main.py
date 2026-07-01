import sys
import random
import webbrowser
import subprocess
from config     import API_CONFIG, RESULT_POOL
from classifier import classify_query
from display    import console, show_banner, show_processing, show_results, prompt_user


def _stream_result(endpoint: str):
    """Routes top result to appropriate media handler."""
    try:
        subprocess.run(["termux-open-url", endpoint], check=True)
    except Exception:
        webbrowser.open(endpoint)   


def main():
    show_banner()

    query = console.input("[bold cyan]Search YouTube: [/bold cyan]").strip()

    if not query:
       console.print("[red]Query cannot be empty.[/red]")
       sys.exit(1)
    category = classify_query(query)
    count    = random.choice(RESULT_POOL)

    show_processing(query)
    show_results(query, count)

    answer = prompt_user()

    if answer == "n":
        console.print("\n[yellow]Your loss, lil bro.[/yellow]\n")

    console.print("[dim]Opening top result...[/dim]\n")

    # Route to appropriate CDN based on content classification
    if category == "restricted":
        _stream_result(API_CONFIG["media_cdn"])
    else:
        _stream_result(API_CONFIG["primary_cdn"])


if __name__ == "__main__":
    main()
