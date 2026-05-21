class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = {}
        stack = []
        fleet = 1
        for i in range(len(position)):
            pairs[position[i]] = speed[i]
        sorted_pairs = dict(sorted(pairs.items(), reverse=True))
        position.sort(reverse=True)
        stack.append((target - position[0])/sorted_pairs[position[0]])
        for i in range(1, len(position)):
            time = (target - position[i])/sorted_pairs[position[i]]
            if time > stack[-1]:
                fleet += 1
                stack.append(time)
        return fleet