class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1

        cur = 0
        ans_idx = 0
        for start_idx in range(n):
            cur += (gas[start_idx] - cost[start_idx])

            if cur < 0:
                ans_idx = start_idx + 1
                cur = 0
        
        return ans_idx
