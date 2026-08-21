class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        seen = [False, False, False]

        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue

            if a == target[0]:
                seen[0] = True
            if b == target[1]:
                seen[1] = True
            if c == target[2]:
                seen[2] = True

        return seen[0] and seen[1] and seen[2]