class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_beg(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head#temp=first node
            while temp:
                print(temp.data," ",end=" ")
                if temp.next!=None:
                    print("->",end=" ")
                #temp.data means first node data
                temp=temp.next
obj=singlelinkedlist()
#node creation-initialising
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
print("before inserting:\n")
obj.display()
print("\nafter inserting:\n")
obj.insert_beg(1000)
obj.display()

