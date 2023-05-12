class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findintersection(head1, head2, d):
    for i in range(d):
        head1 = head1.next
    
    while head1 and head2:
        if head1 is head2:
            return head1.data
        head1 = head1.next
        head2 = head2.next
    return -1

def getintersectionnode(head1, head2):
    c1 = getcount(head1)
    c2 = getcount(head2)
    d = abs(c1-c2)

    if c1 > c2:
        return findintersection(head1, head2, d)
    else:
        return findintersection(head2, head1, d)

def getcount(head):
    temp = head
    count = 0
    while temp:
        count+=1
        temp = temp.next
    return count

common=Node(15)
   
  #Defining first LinkedList
   
head1=Node(3)
head1.next=Node(6)
head1.next.next=Node(9)
head1.next.next.next=common
head1.next.next.next.next=Node(30)

# Defining second LinkedList

head2=Node(10)
head2.next=common
head2.next.next=Node(30)

print("The node of intersection is ",getintersectionnode(head1, head2))

