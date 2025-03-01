# create bfs in some graph defined by adjascency list

from collections import deque

def bfs(g, start):
    # set
    visited = set()
    # queue
    q = deque([start])

    #while queue
    while q:
        
        node = q.popleft() # extract node from leftmost elt of q
        if node not in visited:
            print(node)
            # add node to visited
            visited.add(node)
            #for neighbours of node, add all neighbours to queue
            for neighbour in g[node]:
                if neighbour not in visited:
                    q.append(neighbour)



g1 = {
    "A":["B", "C", "D", "E"],
    "B":["D","E","F"],
    "C":["D","F"],
    "D":["C"],
    "E":["A"],
    "F":[]
}


bfs(g1,"A")