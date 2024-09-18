#level by level, best for shortest path in unweighted graph
from collections import deque

def bfs(graph, start):
    visited = [] 
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)
    
    return visited

graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F', 'G'],
  'D': [],
  'E': ['F'],
  'F': [],
  'G': []
}

#      A
#    /   \
#   B     C 
#  /\     /\
# D  E - F  G
