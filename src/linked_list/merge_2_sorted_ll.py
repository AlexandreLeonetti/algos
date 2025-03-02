# merge 2 sorted ll


class LinkNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next


n6=LinkNode(124,None)
n5=LinkNode(9,n6)
n4=LinkNode(6,n5)
n3=LinkNode(4,n4)
n2=LinkNode(1,n3)
n1=LinkNode(0,n2)




m6=LinkNode(124,None)
m5=LinkNode(8,m6)
m4=LinkNode(8,m5)
m3=LinkNode(4,m4)
m2=LinkNode(2,m3)
m1=LinkNode(0,m2)


def merge(l1, l2):
    dummy = LinkNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Append the remaining nodes of l1 or l2
    current.next = l1 if l1 else l2

    return dummy.next


def show_list(head):
    while(head):
        print(head.val,end = "->")
        head=head.next

print("list 1")
show_list(n1)
print("list2")
show_list(n2)
print("merging...")
merged=merge(n1,m1)
show_list(merged)