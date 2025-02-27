from collections import deque

def bfs_shortest_path(graph, start, target):
    if start not in graph or target not in graph:
        return f"One or both nodes not in graph"
    
    queue = deque([(start, "")])  # Queue stores (current_node, path_to_node) a tuple containing nodes and corresponding paths
    visited = set()
    
    while queue:
        node, path = queue.popleft()  # Dequeue node along with the path
        
        if node not in visited:
            visited.add(node)
            path = path + node  # Append current node to the path, possibly a string
            
            # If we reach the target, return the path
            if node == target:
                return path  
            
            # Enqueue unvisited neighbors with the updated path
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path))
    
    return f"No path found from {start} to {target}"

# Example Graph (Adjacency List Representation)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# Example Usage
start_node, target_node = 'A', 'H'
shortest_path = bfs_shortest_path(graph, start_node, target_node)
print(f"Shortest Path from {start_node} to {target_node}: {shortest_path}")
