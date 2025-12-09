class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hashmap = {} 

        for num in nums:
            if num not in hashmap:
                left = hashmap.get(num-1, 0)
                right = hashmap.get(num+1, 0)
                
                length = left + right + 1
                hashmap[num] = length
                
                hashmap[num - left] = length
                hashmap[num + right] = length

        ans = 0
        for k in hashmap.values():
            ans = max(ans, k)
        
        return ans
        