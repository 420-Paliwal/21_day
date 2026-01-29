class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def printList(head):
    curr = head
    while curr:
        print(curr.val, end = " -> ")
        curr = curr.next
    print("None")

def insertAtHead(head, val):
    newNode = Node(val)
    newNode.next = head
    return newNode

def insertAtEnd(head, val):
    newNode = Node(val)

    if head is None:
        return newNode
    
    curr = head
    while curr.next:
        curr = curr.next
    
    curr.next = newNode
    return head

def deleteAtHead(head):
    if head is None:
        return None
    return head.next

def deleteAtEnd(head):
    if head is None or head.next is None:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head

def deleteByValue(head, target):
    if head is None:
        return None
    
    if head.val == target:
        return head.next
    
    prev = None
    curr = head
    
    while curr:
        if curr.val == target:
            prev.next = curr.next
            return head
        prev = curr
        curr = curr.next
    
    return head


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
printList(head)
head = insertAtHead(head, 5)
printList(head)
head = insertAtEnd(head, 40)
printList(head)
head = deleteAtHead(head)
printList(head)
# head = deleteAtEnd(head)
# printList(head)
# head = deleteByValue(head, 20)
# printList(head)

def delete_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    for _ in range(n+1):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next

    return dummy.next

head = delete_nth_from_end(head, 2)
printList(head)

def rev_list(head):

    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev

head = rev_list(head)
printList(head)


def detect_cycle(head):
    if head is None:
        return False
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False

check_list = detect_cycle(head)
print(check_list)