class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxlen = 1
        l, r = 0, 1
        prev = None

        while r < len(arr):
            if arr[r-1] > arr[r] and (prev is False or prev is None):
                maxlen = max(maxlen, r - l + 1)
                r += 1
                prev = True

            elif arr[r-1] < arr[r] and (prev is True or prev is None):
                maxlen = max(maxlen, r - l + 1)
                r += 1
                prev = False
            else:
                if arr[r-1] == arr[r]:
                    r = r + 1
                l = r - 1
                prev = None

        return maxlen