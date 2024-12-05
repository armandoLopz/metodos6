import numpy as np

def floyd_warshall(graph):
    V = len(graph)
    dist = np.array(graph)
    
    # Initialize path matrix
    path = [[j if graph[i][j] != float('inf') else None for j in range(V)] for i in range(V)]
    
    # Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        path[i][j] = path[i][k]
    
    return dist, path

# Create adjacency matrix for the graph
INF = float('inf')
graph = [
    [0, 2, 4, 3, INF, INF, INF, INF, INF, INF],    # A
    [INF, 0, INF, INF, 7, 6, INF, INF, INF, INF],  # B
    [INF, INF, 0, INF, INF, 2, 4, INF, INF, INF],  # C
    [INF, INF, INF, 0, INF, INF, 5, INF, INF, INF], # D
    [INF, INF, INF, INF, 0, 4, INF, 1, INF, INF],  # E
    [INF, INF, INF, INF, INF, 0, INF, 3, 3, INF],  # F
    [INF, INF, INF, INF, INF, INF, 0, INF, 3, INF], # G
    [INF, INF, INF, INF, INF, INF, INF, 0, INF, 3], # H
    [INF, INF, INF, INF, INF, INF, INF, INF, 0, 4], # I
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0]  # J
]

# Run Floyd-Warshall algorithm
distances, paths = floyd_warshall(graph)

print("Shortest distances matrix:")
print(distances)

# Print shortest distance from A to J
print("\nShortest distance from A to J:", distances[0][9])