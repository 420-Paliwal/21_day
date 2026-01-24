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
head = deleteAtEnd(head)
printList(head)
head = deleteAtEnd(head)
printList(head)
head = deleteAtEnd(head)
printList(head)
head = deleteAtEnd(head)
printList(head)