


class Level1:
    # arrays
    def linear_sort(arr):
        def find_min(a):
            min = a[0]
            for i in range(0,len(a)):
                if a[i]<min:
                    min=a[i]
            return min

        sorted_arr = []
        while arr:
            min_value = find_min(arr)  # Find the minimum element in the array
            sorted_arr.append(min_value)  # Add it to the sorted list
            arr.remove(min_value)  # Remove it from the original array
        return sorted_arr

    # hash table
    def two_sum(nums, target):
        num_map = {}  # Hash table to store number and its index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:  # Check if complement is in hash table
                return [num_map[complement], i]  # Return indices
            num_map[num] = i  # Store index of the number in hash table

        return []  # If no solution found    
    # linked list
    def print_linked_list(head):
        values = []
        while head:
            values.append(str(head.value))
            head = head.next
        print(" -> ".join(values))

    def reverse_linked_list(head):
        prev = None
        current = head

        while current:
            next_node = current.next  # Store next node
            current.next = prev  # Reverse pointer
            prev = current  # Move prev forward
            current = next_node  # Move current forward

        return prev  # New head of reversed list

    
    # trees
    # Inorder traversal: Left -> Root -> Right
    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            print(root.val, end=" ")
            inorder_traversal(root.right)

    # Preorder traversal: Root -> Left -> Right
    def preorder_traversal(root):
        if root:
            print(root.val, end=" ")
            preorder_traversal(root.left)
            preorder_traversal(root.right)

    # Postorder traversal: Left -> Right -> Root
    def postorder_traversal(root):
        if root:
            postorder_traversal(root.left)
            postorder_traversal(root.right)
            print(root.val, end=" ")
    

    # graph
    def bfs(graph, start):
        visited = set()  # Keep track of visited nodes
        queue = deque([start])  # Initialize queue with the starting node

        while queue:
            node = queue.popleft()  # Dequeue a node FIFO
            if node not in visited:
                print(node, end=" ")  # Process the node
                visited.add(node)  # Mark node as visited

                # Enqueue all unvisited neighbors
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)






# Example usage
arr = [5, 3, 8, 1, 2]
sorted_array = Level1.linear_sort(arr)
print("Sorted Array:", sorted_array)

