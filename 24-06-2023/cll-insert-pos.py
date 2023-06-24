#inset at position:
class node:
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
obj.display()             




