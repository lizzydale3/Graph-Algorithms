# Create a new undirected graph
graphy = Graph(directed=False)

# Create a new directed graph
directed_graph = Graph(directed=True)

# Adding vertices and edges
graphy.insert_vertex('A')
graphy.insert_vertex('B')
graphy.insert_edge('A', 'B')

# Get the number of vertices
num_vertices = graphy.num_vertices()
print("Number of vertices:", num_vertices)

# Get the number of edges
num_edges = graphy.num_edges()
print("Number of edges:", num_edges)

# Get all vertices
vertices = graphy.all_vertices()
print("Vertices:", vertices)

# Check if two vertices are adjacent
are_adj = graphy.are_adjacent('A', 'B')
print("Are A and B adjacent?", are_adj)
