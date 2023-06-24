class BST:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    def insert_node(self,data):
        if self.key is None:#check if root node is empty
            print("BST is empty")
            return
        if self.key==data:#check if data already present
            return
        if self.key>data:
            if self.left:
                self.left.insert_node(data)
            else:
                self.left=BST(data)
        else:
            if self.right:
                self.right.insert_node(data)
            else:
                self.right=BST(data)
    def preorder(self):
        print(self.key,end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

l=[1,2,4,5,7,4,8,3,4,5]
obj=BST(5)
for i in l:
    obj.insert_node(i)
obj.preorder()


