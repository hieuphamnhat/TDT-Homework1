class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None
        self.prev = None
class DLinkedList:
    def __init__(self):
        self.head = None
    #insert an item in front of a given doubly linked list.
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
 
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("the given previous node cannot be NULL")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
    #append an item in front of a given doubly linked list.
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return
    def search(self, data):
        headNode = self.head
        while(headNode.next):
            headNode = headNode.next
            if headNode.dataval == data:
                return True
        return False
    def delete(self, data):
        headNode = self.head
        if headNode is not None:
            if headNode.dataval == data:
                self.head = headNode.next
                headNode = None
                return
        while(headNode is not None):
            if headNode.dataval == data:
                break
            prevNode = headNode
            headNode = headNode.next
        if headNode == None:
            return
        prevNode.next = headNode.next
        headNode = None
    def printList(self):
        printval = self.head
        while printval is not None:
            print(printval.dataval)
            printval = printval.next
llist = DLinkedList()
 
# Insert 6. So the list becomes 6->None
llist.append(6)
 
# Insert 7 at the beginning.
# So linked list becomes 7->6->None
llist.push(7)
 
# Insert 1 at the beginning.
# So linked list becomes 1->7->6->None
llist.push(1)
 
# Insert 4 at the end.
# So linked list becomes 1->7->6->4->None
llist.append(4)
 
# Insert 8, after 7.
# So linked list becomes 1->7->8->6->4->None
llist.insertAfter(llist.head.next, 8)
 
print ("Created DLL is: ")
llist.printList()
if llist.search(4):
    print("4 is exist in doubly linked list")
else:
    print("4 doesn't not exist")
llist.delete(7)
llist.printList()