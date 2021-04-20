class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    #iterate through the singly linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    #append some items to the singly linked list
    def appendTo(self, data):
        newNode = Node(data)
        if self.headval is None:
            self.headval = newNode
            return 
        lastNode = self.headval
        while(lastNode.nextval):
            lastNode = lastNode.nextval
        lastNode.nextval = newNode
    #search item in singly linked list
    def search(self, data):
        headNode = self.headval
        while(headNode.nextval):
            headNode = headNode.nextval
            if headNode.dataval == data:
                return True
        return False
    #delete item in singly linked list
    def delete(self, data):
        headNode = self.headval
        if headNode is not None:
            if headNode.dataval == data:
                self.headval = headNode.nextval
                headNode = None
                return
        while(headNode is not None):
            if headNode.dataval == data:
                break
            prevNode = headNode
            headNode = headNode.nextval
        if headNode == None:
            return
        prevNode.nextval = headNode.nextval
        headNode = None
list1 = SLinkedList()
list1.headval = Node("1")
e2 = Node("2")
e3 = Node("3")
list1.headval.nextval = e2
e2.nextval = e3
list1.appendTo("4")
list1.listprint()
if list1.search("2"):
    print("2 is exist in singly linked list")
else:
    print("2 doesn't not exist")
list1.delete("1")
list1.listprint()
