class Solution:
    def children(self, lock):
        res = []
        for i in range(4):
            digit = str((int(lock[i]) + 1) % 10)
            res.append(lock[:i] + digit + lock[i+1:])
            digit = str((int(lock[i]) + 9) % 10)
            res.append(lock[:i] + digit + lock[i+1:])
        return res
            


    def openLock(self, deadends: list[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        queue = deque()
        queue.append(("0000", 0))
        visited = set(deadends)

        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns
            for child in self.children(lock):
                if child not in visited:
                    queue.append((child, turns + 1))
                    visited.add(child)
        
        return -1