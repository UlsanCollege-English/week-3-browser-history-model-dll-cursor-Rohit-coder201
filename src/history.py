# /src/history.py

class _N:
    __slots__ = ("url", "prev", "next")
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cur = None

    def current(self):
        """Return the current URL, or None if empty."""
        return self.cur.url if self.cur else None

    def visit(self, url):
        """If not at the end, drop all forward entries, then append url and move cursor."""
        new_node = _N(url)

        if not self.head:  # empty history
            self.head = self.tail = self.cur = new_node
            return

        if self.cur != self.tail:
            # truncate forward history
            nxt = self.cur.next
            self.cur.next = None
            self.tail = self.cur
            # optional: clean forward nodes
            while nxt:
                nxt.prev = None
                nxt = nxt.next

        # append new node at tail
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.cur = new_node

    def back(self, steps=1):
        """Move backward up to `steps` times and return current URL."""
        while steps > 0 and self.cur and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.current()

    def forward(self, steps=1):
        """Move forward up to `steps` times and return current URL."""
        while steps > 0 and self.cur and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.current()


# --- Test function ---
if __name__ == "__main__":
    # manual test
    h = BrowserHistory()
    h.visit("a"); h.visit("b"); h.visit("c")
    assert h.current() == "c"
    assert h.back() == "b"
    assert h.back() == "a"
    assert h.forward() == "b"
    h.visit("b2")
    assert h.current() == "b2"
    assert h.forward() == "b2"  # no forward left
    print("All tests passed!")
