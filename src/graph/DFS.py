def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set
    
    if node not in visited:
        print(node, end=" ")  # Process the node (printing it)
        visited.add(node)

        for neighbor in graph[node]:  # Visit neighbors recursively
            dfs_recursive(graph, neighbor, visited)





def dfs_iterative(graph, start_node):
    visited = set()  # Track visited nodes
    stack = [start_node]  # Use a stack instead of recursion

    while stack:
        node = stack.pop()  # Get the last inserted element (LIFO)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add neighbors in **reverse order** to maintain correct traversal order
            stack.extend(reversed(graph[node]))  



