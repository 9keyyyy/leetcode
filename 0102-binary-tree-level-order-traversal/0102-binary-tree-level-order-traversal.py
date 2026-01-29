# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans = []
        
        def bfs():
            q = deque([(0, root)])
            while q:
                idx, cur = q.popleft()

                if cur:
                    ans.append([idx, cur])

                    if cur.left:
                        q.append([idx+1, cur.left])
                    if cur.right:
                        q.append([idx+1, cur.right])

        bfs()
        
        res = defaultdict(list)
        for idx, cur in ans:
            res[idx].append(cur.val)

        f = []
        for v in res.values():
            f.append(v)
        
        return f