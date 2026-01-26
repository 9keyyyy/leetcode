# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        stack = []
        curr = root
        
        while stack or curr:
            # 최대한 왼쪽 끝까지 내려가며 스택에 쌓음
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 왼쪽 끝 노드 하나를 꺼냄
            curr = stack.pop()
            k -= 1
            
            # k번째라면 정답 반환
            if k == 0:
                return curr.val
            
            # 오른쪽으로 이동
            curr = curr.right
        