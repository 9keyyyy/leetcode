class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ans = [intervals[0]]

        for cur in intervals:
            s, e = cur[0], cur[1]
            if ans[-1][1] >= s:
                ans[-1][1] = max(e, ans[-1][1])
            else:
                ans.append([s, e])
        
        return ans