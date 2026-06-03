class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word))
            encoded += "#"
            encoded += word
        return encoded


    def decode(self, s: str) -> list[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            
            word = s[j + 1 : j + 1 + length]
            decoded.append(word)
            i = j + length + 1
        return decoded