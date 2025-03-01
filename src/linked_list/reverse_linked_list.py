# reverse a linked list
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # Store next node
        current.next = prev  # Reverse pointer
        prev = current  # Move prev forward
        current = next_node  # Move current forward

    return prev  # New head of reversed list

# Helper function to print the linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(str(head.value))
        head = head.next
    print(" -> ".join(values))

# Example usage
#head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

#hey chatGPT, is the following working as well ?
# like, is it a valid way to initialize a linked list ?
node5 = ListNode(5,None)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = node1
print("Original List:")
print_linked_list(head)

reversed_head = reverse_linked_list(head)
print("\nReversed List:")
print_linked_list(reversed_head)
