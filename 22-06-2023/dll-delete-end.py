#delete at end:
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class doublelinkedlist:
    def __init__(self):
        self.head=None
    def del_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head#temp=first node
            while temp:
                print(temp.data,"",end="")
                if temp.next!=None:
                    print("->",end="")
                #temp.data means first node data
                temp=temp.next
obj=doublelinkedlist()
#node creation-initialising
n=Node(10)
obj.head=n
#print(n.prev)
#print(n.next)
n1=Node(20)
obj.head.next=n1
n1.prev=n
#print(n1.prev)
#print(n1.next)
n2=Node(30)
n1.next=n2
n2.prev=n1
#print(n1.prev)
#print(n1.next)
n3=Node(40)
n2.next=n3
n3.prev=n2
n4=Node(50)
n3.next=n4
n4.prev=n3
#print(n1.prev)
#print(n1.next)
n5=Node(60)
n4.next=n5
n5.prev=n4
#print(n1.prev)
#print(n1.next)
print("before deleting")
obj.display()
print("\nafter deleting")
obj.del_end()
obj.display()
