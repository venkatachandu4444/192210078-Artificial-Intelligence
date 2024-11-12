def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize an empty set to keep track of visited nodes

    visited.add(start)  # Mark the starting node as visited
    print(start, end=" ")  # Print the current node (optional for traversal order display)

    # Traverse all adjacent nodes
    for neighbor in graph[start]:
        if neighbor not in visited:  # Only visit unvisited nodes
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run DFS starting from node 'A'
dfs(graph, 'A')
