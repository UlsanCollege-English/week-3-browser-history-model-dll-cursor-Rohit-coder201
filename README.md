[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hhMLk7hh)
# Browser History Model (DLL + Cursor)

## Story (why this matters)
Real browsers let you click **Back** and **Forward**. But if you go back and then
visit a **new** page, the **forward** history is **discarded**. You’ll implement
that exact behavior with a list and a cursor.

## Technical description (what to build)
`src/history.py` must implement:

- `current()` → url or `None`
- `visit(url)` → if not at the end, **truncate forward** history, then append `url` and move cursor
- `back(steps=1)` → move left up to `steps` times; return current url or `None`
- `forward(steps=1)` → move right up to `steps` times; return current url or `None`

## Hints
1. “Truncate forward” = cut `cur.next` and set `tail = cur`.
2. `back`/`forward` can be small loops stepping while a neighbor exists.
3. Keep a single cursor pointer `cur`.

## Run tests locally
```bash
python -m pytest -q

OR

python -m pytest -q tests/test_history.py
```
## Common problems
- Not truncating forward when visiting after going back.

- Breaking tail when trimming forward.

- Returning a node instead of its url.