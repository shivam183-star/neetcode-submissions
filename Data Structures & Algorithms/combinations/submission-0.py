class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, subset):
            if len(subset) == k:
                res.append(subset.copy())
                return 
            if start > n:
                return
            
            for i in range(start, n + 1):
                subset.append(i)
                backtrack(i+1, subset)

                subset.pop()
                
        
        backtrack(1, [])
        return res