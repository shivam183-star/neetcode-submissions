class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 1
        available = []
        res = []
        n = len(tasks)
        tasks = [[tasks[i][0], tasks[i][1], i] for i in range(n)]
        tasks.sort(key=lambda x:x[0])
        i = 0
        
        while i < n or available:
            if not available and time < tasks[i][0]:
                time = tasks[i][0]
            
            while i < n and time >= tasks[i][0]:
                heapq.heappush(available, (tasks[i][1], tasks[i][2]))
                i += 1
            
            tasktime, index = heapq.heappop(available)
            res.append(index)
            time += tasktime
        return res
