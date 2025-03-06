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

class Level2:
    @staticmethod
    def binary_search(arr, target):
        """Perform binary search on a sorted array.
           Returns the index of target if found, or -1 otherwise."""
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    @staticmethod
    def merge_sort(arr):
        """Sort an array using merge sort."""
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = Level2.merge_sort(arr[:mid])
        right = Level2.merge_sort(arr[mid:])
        return Level2._merge(left, right)
    
    @staticmethod
    def _merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    @staticmethod
    def max_subarray_sum(arr):
        """Return the maximum sum of a contiguous subarray using Kadane's algorithm."""
        if not arr:
            return 0
        max_current = max_global = arr[0]
        for num in arr[1:]:
            max_current = max(num, max_current + num)
            max_global = max(max_global, max_current)
        return max_global

    @staticmethod
    def valid_parentheses(s):
        """Check if the string containing only parentheses/brackets is valid."""
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
        return not stack

    @staticmethod
    def reverse_words(s):
        """Reverse the order of words in a sentence."""
        words = s.split()
        return ' '.join(words[::-1])

    @staticmethod
    def detect_cycle_linked_list(head):
        """Detect if a linked list has a cycle using the fast & slow pointer method.
           (Assumes ListNode is defined in your project.)"""
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    @staticmethod
    def level_order_traversal(root):
        """Perform level-order traversal on a binary tree.
           (Assumes TreeNode is defined in your project.)"""
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result

    @staticmethod
    def is_symmetric(root):
        """Check if a binary tree is symmetric (a mirror of itself)."""
        def is_mirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.value == t2.value and 
                    is_mirror(t1.left, t2.right) and 
                    is_mirror(t1.right, t2.left))
        return is_mirror(root, root)
