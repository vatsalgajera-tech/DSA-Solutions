class TimeMap:

    def __init__(self):
        # key -> list of (timestamp, value)
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        arr = self.map[key]
        left, right = 0, len(arr) - 1
        ans = ""

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return ans