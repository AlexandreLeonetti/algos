# shortest path in graph
from collections import deque

def bfs_shortest_path(g, start, target):
    visited = set()
    q = deque([(start,start)]) # q contains tuples of node and path

    # while queue not empty keep searching
    while q :
        node , path = q.popleft()

        if node not in visited:
           visited.add(node)
           for x in g[node]:
               if x not in visited:
                    path_to_x = path+x
                    q.append((x,path_to_x))
                    if x == target:
                        return path_to_x





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


