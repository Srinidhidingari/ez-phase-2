class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circularlinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
   def insert_beg(self,data):
    newnode=Node(data)
    if self.head is None:
        self.head=newnode
        self.tail=newnode
        tail.next=self.head
    else:
        newnode.next=self.head
        self.head=newnode
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
n1=Node(10)
obj.head=n1
obj.tail=n1
obj.tail.next=obj.head
n2=Node(20)
obj.tail=n2
n1.next=n2
n3=Node(30)
obj.tail=n3
n2.next=n3
n4=Node(40)
obj.tail=n4
n3.next=n4
n5=Node(50)
obj.tail=n5
n4.next=n5
n6=Node(60)
obj.tail=n6
n5.next=n6
print("before inserting")
obj.display()
print("\nafter inserting")
obj.insert_beg(100000000)
obj.display()

#insert at end
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_end(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            self.tail.next=self.head
        else:
            self.tail.next=newnode
            self.tail=newnode
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
                


obj=cll()
#node creation-initializing
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
print("before inserting")
obj.display()
print("\nafter inserting")
obj.insert_end(19)
obj.display()


#inset at position:
"""class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_pos(self,pos,data):
        newnode=node(data)
        if self.head is None:
            
            self.head=newnode
            self.tail=newnode
            self.tail.next=self.head
        else:
            if pos==1:
                insert_beg(data)
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                newnode.next=temp.next
                temp.next=newnode
         
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
obj=cll()
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
obj.insert_pos(2,90)
obj.display()"""              




