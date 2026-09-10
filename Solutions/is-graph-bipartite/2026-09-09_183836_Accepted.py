# Problem: Is Graph Bipartite?
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.8 MB
# Submitted: 2026-09-09_183836 UTC
# URL: https://leetcode.com/submissions/detail/2136752654/

class Solution:
    def bfs(self, graph, visited, u):
        queue = deque()
        visited[u] = 1
        queue.append(u) 
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if visited[v] == visited[u]:
                    return False
                if visited[v] == 0:
                    visited[v] = -visited[u]
                    queue.append(v)
        return True
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [0]*n 
        # if visited[i] = -1 -> setA,  visited[i] = 1 -> setB
        
        for u in range(n):
            if visited[u]==0: 
                if not self.bfs(graph, visited, u):
                    return False

        return True
                        
