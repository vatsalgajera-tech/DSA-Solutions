class PrefixTree:

    def __init__(self):
        self.root = {}
        self.end = "#"

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]

        curr[self.end] = True

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]

        return self.end in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]

        return True