class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        car = []
        for passengers, start, end in trips:
            while car and car[0][0] <= start:
                drop = heapq.heappop(car)
                capacity += drop[1]
            
            if passengers > capacity:
                return False
            
            capacity -= passengers
            heapq.heappush(car, [end, passengers])
        return True