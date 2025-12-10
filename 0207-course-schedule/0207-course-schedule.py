class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        for a, b in prerequisites:
            graph[a].append(b)
        
        def dfs(idx):
            if visited[idx] == 1:
                return False
            if visited[idx] == 2:
                return True
            
            visited[idx] = 1
            
            for neighbor in graph[idx]:
                if not dfs(neighbor):
                    return False
            
            visited[idx] = 2
            return True
        
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False
        
        return True
                

        