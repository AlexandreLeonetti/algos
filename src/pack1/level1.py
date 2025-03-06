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
    # linear sort
    @staticmethod
    def linear_sort(arr):
        def find_min(a) :
            min=0
            for i in range(0,len(a)):
               if a[min]>a[i]:
                   min = i 
            return min
        sorted_arr = []
        while arr:
            min_idx = find_min(arr)
            sorted_arr.append(arr[min_idx])
            arr.pop(min_idx)
        return sorted_arr


    @staticmethod
    def two_sum(arr, target):
        hash_table = {}
        for i,a in enumerate(arr):
            complement = target - a
            if complement in hash_table:
                return [hash_table[complement], i]
            hash_table[a]=i
        return [] 
    
    @staticmethod
    def bfs(graph, start):
        traversal = []
        #visited
        visited = set()
        #queue
        q = deque(start)
        #while still elements in queue just keep exploring
        while q:
            current_node= q.popleft()
            if current_node not in visited:
                visited.add(current_node)
                traversal.append(current_node)

                for neighbour in graph[current_node]:
                    if neighbour not in visited:
                        q.append(neighbour)
        return traversal
    
    @staticmethod
    def preorder_traversal(r):
        result=[]
        def traversal(node):
            if node:
                result.append(node.value)
                traversal(node.left)
                traversal(node.right)
        traversal(r)
        return result
    
    @staticmethod
    def inorder_traversal(r):
        res = []
        def traversal(node):
            if node:
                traversal(node.left)
                res.append(node.value) 
                traversal(node.right)
        traversal(r)
        return res
    
    @staticmethod
    def postorder_traversal(r):
        res=[]
        def traversal(node):
            if node:
                traversal(node.left)
                traversal(node.right)
                res.append(node.value)
        traversal(r)
        return res

    
    class Stack:
        def __init__(self):
            self.stack = []
        def push(self,val):
            self.stack.append(val)

        def pop(self):
            if self.stack:
                return self.stack.pop()
            return None

        def peek(self):
            if self.stack:
                return self.stack[-1]
            return None
        def is_empty(self):
            return len(self.stack)==0
         
    class Queue:
        def __init__(self):
            self.q=deque()

        def enqueue(self,val):
            self.q.append(val)
        
        def dequeue(self):
            if self.q:
                return self.q.popleft()
            return None
        
        def peek(self):
            if self.q:
                return self.q[0]
            return None
        def is_empty(self):
            return len(self.q)==0
                

    @staticmethod
    def reverse_linked_list(head):
        # declare a few pointers
        prev = None
        current = head 
        while current:
            # reverse the next pointer after having saved it
            next_node = current.next
            current.next = prev

            # move the two pointers ahead
            prev = current
            current = next_node
        
        return prev

    @staticmethod
    def find_middle_linked_list(head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    class MinHeap:
        def __init__(self):
            self.heap=[]

        def push(self,val):
            heapq.heappush(self.heap, val)
        
        def pop(self):
            if self.heap:
                return heapq.heappop(self.heap)
            return None

        def peek(self):
            if self.heap:
                return self.heap[0]
            return None

        def is_empty(self):
            return len(self.heap)==0
        

    class TrieNode:
        def __init__(self):
            self.is_end_of_word = False
            self.children = {}
    
    class Trie:
        def __init__(self):
            self.root = Level1.TrieNode()
        
        def search (self, word):
            # for char in word, if char in node.children then node= node.children[char]
            node = self.root
            for char in word:
                if char not in node.children:
                    return False
                node = node.children[char]
            return node.is_end_of_word
        
        def insert(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = Level1.TrieNode()
                node=node.children[char]
            node.is_end_of_word=True

        
        def starts_with(self, prefix):
            # check if prefix exists
            node = self.root
            for char in prefix:
                if char not in node.children:
                    return False
                node = node.children[char]
            return True
