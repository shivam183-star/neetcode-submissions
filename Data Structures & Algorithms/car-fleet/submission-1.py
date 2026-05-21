class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        stack = []
        fleet = 1
        
        pairs.sort(reverse=True)
        stack.append((target - pairs[0][0])/pairs[0][1])
        for i in range(1, len(position)):
            time = (target - pairs[i][0])/pairs[i][1]
            if time > stack[-1]:
                fleet += 1
                stack.append(time)
        return fleet
        
