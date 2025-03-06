# test_levels.py

import unittest
from src.pack1.level1 import Level1, TreeNode, ListNode  # import the class/functions you want to test

class TestLevel1(unittest.TestCase):
    def test_linear_sort(self):
        # Test normal case
        self.assertEqual(Level1.linear_sort([4, 2, 7, 1]), [1, 2, 4, 7])
        # Test empty array
        self.assertEqual(Level1.linear_sort([]), [])
        # Test already sorted
        self.assertEqual(Level1.linear_sort([1, 2, 3]), [1, 2, 3])

    def test_two_sum(self):
        # Typical case
        self.assertEqual(Level1.two_sum([2, 7, 11, 15], 9), [0, 1])
        # Case with negative numbers
        self.assertEqual(Level1.two_sum([-3, 4, 3, 90], 0), [0, 2])
        # No solution case
        self.assertEqual(Level1.two_sum([1, 2, 3], 6), [])

    def test_bfs(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E']
        }
        # BFS should visit nodes in a typical BFS order from start 'A'
        self.assertEqual(Level1.bfs(graph, 'A'), ['A', 'B', 'C', 'D', 'E', 'F'])


    def test_tree_traversals(self):
        """
        Tree structure:
                1
               / \
              2   3
             / \
            4   5
        """

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)


        self.assertEqual(Level1.preorder_traversal(root),[1,2,4,5,3])
        self.assertEqual(Level1.inorder_traversal(root),[4,2,5,1,3])
        self.assertEqual(Level1.postorder_traversal(root),[4,5,2,3,1])

    # --- STACK ---
    def test_stack(self):
        stack = Level1.Stack()
        self.assertTrue(stack.is_empty())
        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.is_empty())

    # --- QUEUE ---
    def test_queue(self):
        queue = Level1.Queue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertTrue(queue.is_empty())

    # --- LINKED LIST ---
    def test_reverse_linked_list(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        new_head = Level1.reverse_linked_list(head)
        result = []
        while new_head:
            result.append(new_head.val)
            new_head = new_head.next
        self.assertEqual(result, [4, 3, 2, 1])

    def test_find_middle_linked_list(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual(Level1.find_middle_linked_list(head).val, 3)

        head_even = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        self.assertEqual(Level1.find_middle_linked_list(head_even).val, 4)

    # --- MIN HEAP ---
    def test_min_heap(self):
        heap = Level1.MinHeap()
        heap.push(10)
        heap.push(5)
        heap.push(20)
        self.assertEqual(heap.peek(), 5)
        self.assertEqual(heap.pop(), 5)
        self.assertEqual(heap.pop(), 10)
        self.assertEqual(heap.pop(), 20)
        self.assertTrue(heap.is_empty())

    # --- TRIE ---
    def test_trie(self):
        trie = Level1.Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.starts_with("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))

if __name__ == "__main__":
    unittest.main()
