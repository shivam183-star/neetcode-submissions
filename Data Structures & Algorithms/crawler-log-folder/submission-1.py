class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder = 0
        for log in logs:
            if log == "../":
                if folder > 0:
                    folder -= 1
            elif log == "./":
                continue
            else:
                folder += 1
        return folder