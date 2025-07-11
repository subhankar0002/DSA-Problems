class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#create Node     
val1=Node(5)
val2=Node(6)
val3=Node(4)
val4=Node(10)
val5=Node(9)
val6=Node(1)
head=val1
val1.next=val2
val2.next=val3
val3.next=val4
val4.next=val5
val5.next=val6

#Printing List
def traverse(head):
    current=head
    while current:
        print(current.data)
        current=current.next
traverse(head)

#shorting Data




