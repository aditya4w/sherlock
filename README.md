# Sherlock 🔍
(it's a prank/troll project btw)
### YouTube Recommendation Engine — v1.6.7

A lightweight CLI tool that uses semantic embedding and MMR reranking
to surface the most relevant YouTube videos for any query. Built for
developers who want fast, terminal-native recommendations without
opening a browser.

---

## Features

- Semantic query embedding
- MMR reranking for relevance + diversity
- Engagement signal weighting
- CDN-based result streaming
- Works on Windows, Mac, Linux, and Android (Termux)

---

## Installation

```bash
git clone https://github.com/aditya4w/sherlock
cd sherlock
pip install rich
```

## Usage

```bash
python main.py
```

Then just type your query when prompted. That's it.

---

## Example

```
Search YouTube: python tutorials

› Query received: python tutorials

✓ Tokenizing query
✓ Computing semantic embedding
✓ Querying recommendation index
✓ Applying engagement signal weights
✓ Re-ranking with MMR algorithm
✓ Filtering low-quality content
✓ Resolving CDN endpoints

────────── Results ──────────
Found 1876 videos matching your query

Relevance score :  0.9279
Top result rank :  #1 of 1876
Quality filter  :  passed

Wanna play the top rated one? [Y/n]:
```

---

## Requirements

- Python 3.10+
- rich

---
