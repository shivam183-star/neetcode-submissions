class Solution:
    def possible(self, capacity, weights, days):
        available = capacity
        d = 1
        for w in weights:
            if available < w:
                d += 1
                available = capacity
            available -= w
        if d <= days:
            return True
        else:
            return False


    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high)//2
            if self.possible(mid, weights, days):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans