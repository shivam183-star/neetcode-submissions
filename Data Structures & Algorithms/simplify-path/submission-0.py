class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        new = path.split("/")
        for ch in new:
            if ch == "..":
                if stack:
                    stack.pop()
            elif ch != "." and ch != "":
                stack.append(ch)
        return "/" + "/".join(stack)