#delete at beg
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circularlinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def del_beg(self):
         if self.head is None:
            print("no linked list")
         else:
            temp=self.head
            temp.next=self.head
            temp.next=None
            self.tail.next=self.head
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head#temp assigned to first node
            while temp.next!=self.head:
                if temp.next is None:
                    temp.next=self.head
                else:
                    print(temp.data,'->',end=' ')
                    temp=temp.next
            print(self.head.data)
                

obj=circularlinkedlist()

n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
obj.display()
obj.del_beg()
obj.display()


