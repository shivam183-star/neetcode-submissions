class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def backtrack(i, target, subset):
            if target == 0:
                result.append(subset.copy())
                return
              
            if i >= len(candidates) or target < 0:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
            
                subset.append(candidates[j])

                backtrack(j+1, target - candidates[j], subset)
                subset.pop()
            

        backtrack(0, target, [])
        return result