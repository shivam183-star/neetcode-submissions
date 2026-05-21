class Solution:
    def Merge(self, nums, l, r, m):
        n1 = m - l + 1
        n2 = r - m
        L = [0]*(n1+1)
        R = [0]*(n2+1)
        for i in range(n1):
            L[i] = nums[l + i]
        for j in range(n2):
            R[j] = nums[m + 1 + j]
        L[n1] = float('inf')
        R[n2] = float('inf')
        i = 0
        j = 0
        for k in range(l, r+1):
            if L[i] >= R[j]:
                nums[k] = R[j]
                j += 1
            else:
                nums[k] = L[i]
                i += 1

    def mergeSort(self, nums, l, r):
        if l < r:
            m = (l+r)//2
            self.mergeSort(nums, l, m)
            self.mergeSort(nums, m+1, r)
            self.Merge(nums, l, r, m)


    def sortArray(self, nums: list[int]) -> list[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

