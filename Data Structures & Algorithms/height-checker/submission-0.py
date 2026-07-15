class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count += 1
        return count