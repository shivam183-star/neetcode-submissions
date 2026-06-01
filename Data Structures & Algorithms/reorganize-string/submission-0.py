class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        freq = Counter(s)
        if max(freq.values()) > (len(s) + 1)//2:
            return ""
        heap = [(-v, k) for k, v in freq.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            f1, c1 = heapq.heappop(heap)
            f2, c2 = heapq.heappop(heap)

            res += c1 + c2
            if f1 + 1:
                heapq.heappush(heap, (f1 + 1, c1))
            if f2 + 1:
                heapq.heappush(heap, (f2 + 1, c2))
        if heap:
            res += heap[0][1]
        return res