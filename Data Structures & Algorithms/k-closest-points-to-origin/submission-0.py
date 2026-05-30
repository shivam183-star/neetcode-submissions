class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for i in range(len(points)):
            points[i] = (points[i][0]**2 + points[i][1]**2, points[i])
        heapq.heapify(points)

        for i in range(k):
            result.append(heapq.heappop(points)[1])
        return result