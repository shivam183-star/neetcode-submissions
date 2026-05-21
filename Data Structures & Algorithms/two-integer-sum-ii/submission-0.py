class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        res = []
        while left < right:
            if numbers[left] + numbers[right] == target:
                res.append(left + 1)
                res.append(right + 1)
                return res
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1