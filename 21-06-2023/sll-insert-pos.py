#insert in between
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_between(self,pos,data):
        newnode=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data," ",end=" ")
                if temp.next!=None:
                    print("->",end=" ")
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
obj.insert_between(3,1000)
obj.display()
