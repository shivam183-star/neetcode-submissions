class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capitalHeap = []
        profitHeap = []

        for c, p in zip(capital, profits):
            heapq.heappush(capitalHeap, (c, p))
        
        for i in range(k):
            while capitalHeap and capitalHeap[0][0] <= w:
                c, p = heapq.heappop(capitalHeap)
                heapq.heappush(profitHeap, -p)
            
            if not profitHeap:
                return w
            
            w += -heapq.heappop(profitHeap)

        return w
