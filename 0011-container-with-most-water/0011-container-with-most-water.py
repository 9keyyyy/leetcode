class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        n = len(height)
        s, e = 0, n-1

        ans = 0
        while s < e:
            w = e - s
            h = min(height[s], height[e])
            ans = max(ans,  h*w)

            if height[s] == h:
                s += 1
            else:
                e -= 1
                
        return ans