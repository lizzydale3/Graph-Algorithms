# Graph Algorithms 📈

This repository contains essential graph algorithms, covering common use cases, approaches, and tips for handling edge cases. These algorithms are fundamental for solving a variety of problems related to connectivity, pathfinding, and data structure traversal.

## Table of Contents
- [Breadth-First Search (BFS)](#breadth-first.py)
- [Depth-First Search (DFS)](#depth-first.py)

- [Dijkstra’s Algorithm](#dijkstras-algorithm)
- [Minimum Spanning Tree (MST)](#minimum-spanning-tree-mst)
- [Topological Sort](#topological-sort)

---

### Breadth-First Search (BFS)

**Use Case**: BFS is ideal for finding the shortest path in unweighted graphs and for level-order traversal.

**Approach**:
1. Initialize a queue and add the starting node.
2. Mark nodes as visited as you explore each node level by level.
3. Process each neighbor of the node and add unvisited neighbors to the queue.

**Edge Cases**:
- **Disconnected Graphs**: If the graph is not fully connected, ensure isolated nodes are handled.
- **Cycles**: Implement checks to avoid revisiting nodes.
