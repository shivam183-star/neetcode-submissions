class TimeMap:

    def __init__(self):
        self.maps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.maps.keys():
            self.maps[key].append((value, timestamp))
        else:
            self.maps[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.maps.keys():
            return ""
        ans = ""
        low = 0
        high = len(self.maps[key]) - 1
        while low <= high:
            mid = (low + high)//2
            if self.maps[key][mid][1] <= timestamp:
                ans = self.maps[key][mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return ans