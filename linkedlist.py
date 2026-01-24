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

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head = insertAtHead(head, 5)
head = insertAtEnd(head, 40)
head = deleteAtHead(head)
printList(head)