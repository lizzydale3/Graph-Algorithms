class Graph:
    def __init__(self, directed=False):
        self.adjacency_list = {}  # dictionary to store adjacency list
        self.directed = directed  # flag to check if the graph is directed

    # Number of vertices
    def num_vertices(self):
        return len(self.adjacency_list)

    # Number of edges
    def num_edges(self):
        count = sum(len(edges) for edges in self.adjacency_list.values())
        if not self.directed:
            count //= 2
        return count

    # Return all vertices
    def all_vertices(self):
        return list(self.adjacency_list.keys())

    # Return all edges
    def all_edges(self):
        edges = []
        for vertex, adj in self.adjacency_list.items():
            for neighbor in adj:
                if self.directed or (neighbor, vertex) not in edges:
                    edges.append((vertex, neighbor))
        return edges

    # Return a vertex
    def some_vertex(self):
        if self.adjacency_list:
            return next(iter(self.adjacency_list))
        return None

    # Degree of a vertex
    def degree(self, v):
        if v in self.adjacency_list:
            return len(self.adjacency_list[v])
        return None

    # Edges incident upon a vertex
    def edges_incident(self, v):
        if v in self.adjacency_list:
            return [(v, neighbor) for neighbor in self.adjacency_list[v]]
        return None

    # Vertices adjacent to a vertex
    def adjacent_vertices(self, v):
        if v in self.adjacency_list:
            return list(self.adjacency_list[v])
        return None

    # Return two end vertices of an edge
    def end_vertices(self, e):
        if e in self.all_edges():
            return e[0], e[1]
        return None

    # Check if two vertices are adjacent
    def are_adjacent(self, v1, v2):
        if v1 in self.adjacency_list and v2 in self.adjacency_list[v1]:
            return True
        return False

    # Check if an edge is directed
    def is_directed(self, e):
        return self.directed

    # In-degree of a vertex
    def in_degree(self, v):
        if self.directed and v in self.adjacency_list:
            count = 0
            for vertex in self.adjacency_list:
                if v in self.adjacency_list[vertex]:
                    count += 1
            return count
        return None

    # Incoming or outgoing edges incident upon a vertex
    def edges_incident_dir(self, v, incoming=True):
        edges = []
        if self.directed:
            if incoming:
                for vertex, adj in self.adjacency_list.items():
                    if v in adj:
                        edges.append((vertex, v))
            else:
                edges = [(v, neighbor) for neighbor in self.adjacency_list[v]]
        return edges

    # Vertices adjacent along incoming or outgoing edges
    def adjacent_vertices_dir(self, v, incoming=True):
        adj_vertices = []
        if self.directed:
            if incoming:
                for vertex, adj in self.adjacency_list.items():
                    if v in adj:
                        adj_vertices.append(vertex)
            else:
                adj_vertices = list(self.adjacency_list[v])
        return adj_vertices

    # Insert a new edge
    def insert_edge(self, v1, v2):
        if v1 not in self.adjacency_list:
            self.adjacency_list[v1] = set()
        if v2 not in self.adjacency_list:
            self.adjacency_list[v2] = set()
        self.adjacency_list[v1].add(v2)
        if not self.directed:
            self.adjacency_list[v2].add(v1)

    # Insert a new vertex
    def insert_vertex(self, v):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = set()

    # Remove an edge
    def remove_edge(self, v1, v2):
        if v1 in self.adjacency_list and v2 in self.adjacency_list[v1]:
            self.adjacency_list[v1].remove(v2)
        if not self.directed and v2 in self.adjacency_list and v1 in self.adjacency_list[v2]:
            self.adjacency_list[v2].remove(v1)

    # Remove a vertex and all its incident edges
    def remove_vertex(self, v):
        if v in self.adjacency_list:
            # Remove all edges incident to this vertex
            for neighbor in self.adjacency_list[v]:
                self.adjacency_list[neighbor].remove(v)
            del self.adjacency_list[v]
