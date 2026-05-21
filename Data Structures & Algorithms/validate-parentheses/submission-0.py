class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for ch in s:
            if ch in mapping:
                if not stack or mapping[ch] != stack.pop():
                    return False
            else:
                stack.append(ch)
        if stack:
            return False
        else:
            return True
