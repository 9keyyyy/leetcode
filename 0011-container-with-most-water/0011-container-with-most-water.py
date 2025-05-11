class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s, e = 0, len(height)-1

        ans = (e - s) * min(height[s], height[e])
        while True:
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
            
            if s == e:
                break
            
            cur = (e - s) * min(height[s], height[e])

            if ans < cur:
                ans = cur

        return ans

