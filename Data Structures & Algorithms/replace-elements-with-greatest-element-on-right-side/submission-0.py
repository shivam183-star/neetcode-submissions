class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxele = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            ele = arr[i]
            arr[i] = maxele
            maxele = max(ele, maxele)
        
        return arr
