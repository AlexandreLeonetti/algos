# does a list have cycle inside ?


#Input: 3 -> 2 -> 0 -> -4 -> (points back to node 2)
#Output: True (Cycle detected)


class LinkNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def hasCycle(head):#floyd cycle detection
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next  # Moves one step
        fast = fast.next.next  # Moves two steps

        if slow == fast:  # If they meet, cycle exists
            return True

    return False  # No cycle




m6=LinkNode(124,None)
m5=LinkNode(8,m6)
m4=LinkNode(8,m5)
m3=LinkNode(4,m4)
m2=LinkNode(2,m3)
m1=LinkNode(0,m2)




c6=LinkNode(124,None)
c5=LinkNode(8,c6)
c4=LinkNode(8,None)
c3=LinkNode(4,c4)
c2=LinkNode(2,c3)
c1=LinkNode(0,c2)
c4.next=c2

print(hasCycle(m1))
print(hasCycle(c1))
