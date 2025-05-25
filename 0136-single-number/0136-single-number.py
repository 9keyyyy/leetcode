class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = defaultdict(int)

        for n in nums:
            arr[n] += 1

        for k, v in arr.items():
            if v == 1:
                return k
        