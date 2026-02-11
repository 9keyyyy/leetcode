class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            degree[course] += 1

        q = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)

        ans = []
        while q:
            c = q.popleft()
            ans.append(c)
            
            for n in graph[c]:
                degree[n] -= 1
                if degree[n] == 0:
                    q.append(n)
        
        return ans if len(ans) == numCourses else []


        