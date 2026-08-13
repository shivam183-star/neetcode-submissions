class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        freq = Counter(hand)
        heap = list(freq.keys())
        heapq.heapify(heap)

        group = groupSize

        while heap:
            num = heap[0]
            for i in range(num, num + groupSize):
                if i not in freq:
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    if i!= heap[0]:
                        return False
                    heapq.heappop(heap)

        return True