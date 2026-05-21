class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = 0
        string = ""
        for ch in s:
            if ch == "[":
                stack.append((string, current))
                string = ""
                current = 0
            elif ch == "]":
                prev, num = stack.pop()
                string = prev + (num*string)
            elif ch.isdigit():
                current = current*10 + int(ch)
            else:
                string += ch
        return string