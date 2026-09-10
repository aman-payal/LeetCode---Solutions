# Problem: Is Graph Bipartite?
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.9 MB
# Submitted: 2026-09-09_181255 UTC
# URL: https://leetcode.com/submissions/detail/2136720991/

class Solution:
    def dfs(self, graph, visited, u):
        queue = deque()
        visited[u] = 1
        queue.append(u) 
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if visited[v] == visited[u]:
                    return False
                if visited[v] == 0:
                    visited[v] = visited[u]*(-1)
                    queue.append(v)
        return True



    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        m = len(graph[0])
        visited = [0]*n # -1 = setA,  1=  setB
        
        for u in range(n):
            if visited[u]==0:
                if not self.dfs(graph, visited, u):
                    return False
        return True
                        
