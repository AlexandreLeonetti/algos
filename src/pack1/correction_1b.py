# levels.py

from collections import deque
import heapq

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class ListNode:
    """ Basic ListNode class for linked lists """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Level1:
    # level 1 arrays
    @staticmethod
    def linear_sort(arr):
        """
        returns a sorted array
        """
        def find_min(a):
            min = a[0]
            for i in range(0, len(a)):
                if min > a[i]:
                    min = a[i]

            return min

        sorted_arr = []
        while arr:
            m = find_min(arr)
            sorted_arr.append(m)
            arr.remove(m)
        return sorted_arr
    
    @staticmethod
    def linear_sort_index(arr):
        def find_min(a):
            min_idx = 0
            for i in range(0, len(a)):
                if arr[min_idx]> arr[i]:
                    min_idx = i
            return min_idx
        
        sorted_arr = []
        while arr:
            m_idx = find_min(arr)
            sorted_arr.append(arr[m_idx])
            arr.pop(m_idx)
            #sorted_arr.append(arr.pop(mid_idx))
        return sorted_arr

    @staticmethod
    def two_sum(nums, target):
        """
        Return indices of the two numbers such that they add up to target.
        """
        hash_table = {}

        for i,num in enumerate(nums):
            complement = target - num 
            if complement in hash_table:
                return[ hash_table[complement],i]
            hash_table[num]=i

        return []

    #level1 graph
    @staticmethod
    def bfs(graph, start):
        """
        Perform Breadth-First Search (BFS) on the given graph from start node.
        Return the order in which the nodes are visited. an array of characters
        """
        order = []
        visited = set()
        queue = deque([start])

        while(queue):
            current_node = queue.popleft()
            if current_node not in visited:
                order.append(current_node)
                visited.add(current_node)
                for neighbour in graph[current_node]:
                    if neighbour not in visited:
                        queue.append(neighbour)

        return order
    
    # You can keep adding more data structure related functions here...
    # level1 binary trees
    @staticmethod
    def preorder_traversal(r):
        result = []
        def traversal(x):
            if x:
                result.append(x.value)
                traversal(x.left)
                traversal(x.right)
        traversal(r)
        return result

    def inorder_traversal(r):
        result = []
        def traversal(node):
            if node:
                traversal(node.left)
                result.append(node.value)
                traversal(node.right)
        traversal(r)
        return result

    def postorder_traversal(r):
        result=[]
        def traversal(node):
            if node:
                traversal(node.left)
                traversal(node.right)
                result.append(node.value)
        traversal(r)
        return result
    
    # --- LEVEL 1 STACK (LIFO) ---
    class Stack:
        """
        Simple stack implementation using a list.
        """
        def __init__(self):
            self.stack = []

        def push(self, val):
            self.stack.append(val)

        def pop(self):
            if self.stack:
                return self.stack.pop()
            return None

        def peek(self):
            return self.stack[-1] if self.stack else None

        def is_empty(self):
            return len(self.stack) == 0

    # --- LEVEL 1 QUEUE (FIFO) ---
    class Queue:
        """
        Simple queue implementation using collections.deque
        """
        def __init__(self):
            self.queue = deque()

        def enqueue(self, val):
            self.queue.append(val)

        def dequeue(self):
            if self.queue:
                return self.queue.popleft()
            return None

        def peek(self):
            return self.queue[0] if self.queue else None

        def is_empty(self):
            return len(self.queue) == 0

    # --- LEVEL 1 LINKED LIST (Basic Operations) ---
    @staticmethod
    def reverse_linked_list(head):
        """
        Reverse a singly linked list.
        """
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev  # New head of reversed list

    @staticmethod
    def find_middle_linked_list(head):
        """
        Find the middle node of a linked list.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow  # Middle node

    # --- LEVEL 1 HEAP (Min Heap using heapq) ---
    import heapq
    class MinHeap:
        """
        Basic min-heap implementation using heapq.
        """
        def __init__(self):
            self.heap = []

        def push(self, val):
            heapq.heappush(self.heap, val)

        def pop(self):
            return heapq.heappop(self.heap) if self.heap else None

        def peek(self):
            return self.heap[0] if self.heap else None

        def is_empty(self):
            return len(self.heap) == 0

    # --- LEVEL 1 TRIE (Basic Implementation) ---
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end_of_word = False

    class Trie:
        """
        Basic Trie (Prefix Tree) implementation.
        """
        def __init__(self):
            self.root = Level1.TrieNode()

        def insert(self, word):
            """
            Insert a word into the Trie.
            """
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = Level1.TrieNode()
                node = node.children[char]
            node.is_end_of_word = True

        def search(self, word):
            """
            Search for a word in the Trie.
            Returns True if the word exists, otherwise False.
            """
            node = self.root
            for char in word:
                if char not in node.children:
                    return False
                node = node.children[char]
            return node.is_end_of_word

        def starts_with(self, prefix):
            """
            Check if there exists any word in the Trie that starts with the given prefix.
            """
            node = self.root
            for char in prefix:
                if char not in node.children:
                    return False
                node = node.children[char]
            return True