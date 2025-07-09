class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int] 
        """
        # 입력 배열의 길이
        length = len(nums)
        # 왼쪽, 오른쪽, 답
        L, R, answer = [0] * length, [0] * length, [0] * length
       
        # L[i]는 왼쪽에 있는 모든 원소들의 곱 포함
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
       
        # R[i]는 오른쪽에 있는 모든 원소들의 곱 포함
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]
       
        for i in range(length):
            answer[i] = L[i] * R[i]
       
        return answer
