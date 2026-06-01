class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a:
            heap.append((-a, "a"))
        if b:
            heap.append((-b, "b"))
        if c:
            heap.append((-c, "c"))
        heapq.heapify(heap)
        res = ""
        while heap:
            count, char = heapq.heappop(heap)
            if len(res) >= 2 and char == res[-1] and char == res[-2]:
                if heap:
                    newcount, newchar = heapq.heappop(heap)
                else:
                    return res
                res += newchar
                if newcount + 1:
                    heapq.heappush(heap, (newcount + 1, newchar))
                heapq.heappush(heap, (count, char))
            else:
                res += char
                if count + 1:
                    heapq.heappush(heap, (count + 1, char))
        return res
