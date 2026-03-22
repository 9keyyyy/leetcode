class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        dist[0] = 0

        graph = {}
        for i in range(1, n+1):
            graph[i] = []

        for s, e, v in times:
            graph[s].append((e, v))


        heap = [(0, k)]
        while heap:
            cur_dist, cur_node = heapq.heappop(heap)
            
            if cur_dist > dist[cur_node]:
                continue

            for e, v in graph[cur_node]:
                new_dist = cur_dist + v

                if dist[e] > new_dist:
                    dist[e] = new_dist
                    heapq.heappush(heap, (new_dist, e))

        return max(dist) if max(dist) != float('inf') else -1
            
        