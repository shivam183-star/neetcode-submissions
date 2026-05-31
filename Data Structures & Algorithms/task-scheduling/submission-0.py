class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-val for val in freq.values()]
        heapq.heapify(heap)
        time = 0
        cooldown = deque()
        while heap or cooldown:
            time += 1
            if heap:
                exe= heapq.heappop(heap)
                if exe + 1 != 0:
                    cooldown.append((exe + 1, time + n))

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(heap, cooldown.popleft()[0])
                
        return time