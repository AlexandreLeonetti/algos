import unittest
from src.pack2.level2 import Level2, TreeNode, ListNode  # Adjust the import path as needed

class TestLevel2(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(Level2.binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(Level2.binary_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(Level2.binary_search([], 1), -1)

    def test_merge_sort(self):
        self.assertEqual(Level2.merge_sort([4, 2, 7, 1]), [1, 2, 4, 7])
        self.assertEqual(Level2.merge_sort([]), [])
        self.assertEqual(Level2.merge_sort([1, 2, 3]), [1, 2, 3])

    def test_max_subarray_sum(self):
        self.assertEqual(Level2.max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(Level2.max_subarray_sum([1, 2, 3, 4]), 10)
        self.assertEqual(Level2.max_subarray_sum([]), 0)

    def test_valid_parentheses(self):
        self.assertTrue(Level2.valid_parentheses("()[]{}"))
        self.assertFalse(Level2.valid_parentheses("([)]"))
        self.assertTrue(Level2.valid_parentheses(""))

    def test_reverse_words(self):
        self.assertEqual(Level2.reverse_words("hello world"), "world hello")
        self.assertEqual(Level2.reverse_words("a b c"), "c b a")
        self.assertEqual(Level2.reverse_words("single"), "single")

    def test_detect_cycle_linked_list(self):
        # Create a linked list without cycle: 1 -> 2 -> 3 -> None
        node3 = ListNode(3)
        node2 = ListNode(2, node3)
        node1 = ListNode(1, node2)
        self.assertFalse(Level2.detect_cycle_linked_list(node1))
        
        # Create a linked list with a cycle: 1 -> 2 -> 3 -> 2 ...
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        node3.next = node2  # Cycle here
        self.assertTrue(Level2.detect_cycle_linked_list(node1))

    def test_level_order_traversal(self):
        # Build a binary tree:
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(Level2.level_order_traversal(root), [[1], [2, 3], [4, 5]])

    def test_is_symmetric(self):
        # Symmetric tree:
        #       1
        #      / \
        #     2   2
        #    / \ / \
        #   3  4 4  3
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3), TreeNode(4))
        root.right = TreeNode(2, TreeNode(4), TreeNode(3))
        self.assertTrue(Level2.is_symmetric(root))
        
        # Non-symmetric tree:
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertFalse(Level2.is_symmetric(root))

if __name__ == '__main__':
    unittest.main()
