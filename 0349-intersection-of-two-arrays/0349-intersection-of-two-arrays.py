class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = Counter(nums1)
        b = Counter(nums2)

        arr = []
        for k, v in a.items():
            if k in b:
                arr.append(k)

        return arr