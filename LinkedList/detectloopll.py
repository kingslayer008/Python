class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def detectloop(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
 
# Create a loop for testing
llist.head.next.next.next.next = llist.head
if(llist.detectloop()):
    print("Loop Found")
else:
    print("No Loop")