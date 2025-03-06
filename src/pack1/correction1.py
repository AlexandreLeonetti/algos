# levels.py

from collections import deque

class Level1:
    @staticmethod
    def linear_sort(arr):
        """
        Sort the array in ascending order using a simple approach (like selection sort).
        """
        sorted_arr = []
        # Basic approach: find min and remove from arr until arr is empty
        while arr:
            min_val = min(arr)
            sorted_arr.append(min_val)
            arr.remove(min_val)
        return sorted_arr

    @staticmethod
    def two_sum(nums, target):
        """
        Return indices of the two numbers such that they add up to target.
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

    @staticmethod
    def bfs(graph, start):
        """
        Perform Breadth-First Search (BFS) on the given graph from start node.
        Return the order in which the nodes are visited.
        """
        visited = set()
        queue = deque([start])
        order = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                order.append(node)
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return order
    
    # You can keep adding more data structure related functions here...

class Level2:
    """
    Another level with more complex algorithms or data structures.
    """
    # placeholder for advanced exercises
    pass
