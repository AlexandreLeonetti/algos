# bfs applied to finding shortest path

from collections import deque


def sp( g, start, target):
    #visited set
    visited = set()
    # queue tuples
    q = deque([(start, start)]) # tuple(node, path)   path is just concatenated string of node names


    while q:
        # extract tuple (node, path) (node )to visit from queue
        node, path = q.popleft()
        # add it to visited if not visited set if not visited yet
        if node == target:
            return path
        if node not in visited:
            visited.add(node)
        # for each neighbour of node, add neighbour to queue if not visited yet
        # make sure to concat new node to path
            for neighbour in g[node]:
                if neighbour not in visited:
                    further_path = path+neighbour
                    q.append((neighbour,further_path))



g1 = {
    "A":["B","C"],
    "B":["C","D","A"],
    "C":["B","D"],
    "D":["C","E"],
    "E":["A"]
}


print(sp(g1,"A","E"))