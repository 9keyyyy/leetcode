class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        major_len = math.ceil(n/2)
        hmap = defaultdict(int)

        for n in nums:
            hmap[n] += 1
            if hmap[n] >= major_len:
                return n

