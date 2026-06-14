class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        total = sum(matchsticks)

        if total % 4 != 0:
            return False
        
        oneside = total / 4
        matchsticks.sort(reverse=True)
        
        def dfs(i, sides):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if matchsticks[i] + sides[j] > oneside:
                    continue
                
                sides[j] += matchsticks[i]
                if dfs(i+1, sides):
                    return True
                sides[j] -= matchsticks[i]

                if sides[j] == 0:
                    break
                
            return False
        

    
        return dfs(0, [0] * 4)

