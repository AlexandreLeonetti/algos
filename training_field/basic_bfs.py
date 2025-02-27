# bfs search
from collections import deque 


def bfs(graph, start):
    visited = set()
    q = deque([start]) 

    while q : # while the queue contains more than zero elements
        # current node is leftmost queue popped element
        node = q.popleft()
        if node not in visited:
            # add node to visited set
            visited.add(node)
            # print visited node
            print(f"visited {node}")

            # for each element of the node in the graph add them to the queue
            for x in graph[node]:
                if x not in visited:
                    q.append(x)
            







# example bfs with adjascency list representation

g1 = {
    "A":["B","C"],
    "B":["A","C","E"],
    "C":["D"],
    "D":["C"],
    "E":["B"]
}

bfs(g1,"A")


