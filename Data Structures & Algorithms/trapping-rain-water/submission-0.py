class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [0]
        maxi = height[0]
        for i in range(1, len(height)):
            maxleft.append(maxi)
            maxi = max(height[i], maxi)

        maxright = [0]
        rev = list(reversed(height))

        maxi = rev[0]
        for i in range(1, len(height)):
            maxright.append(maxi)
            maxi = max(rev[i], maxi)
        maxright.reverse()
        volume = 0

        for i in range(len(height)):
            w = min(maxleft[i], maxright[i]) - height[i]
            if w > 0:
                volume += w
        return volume