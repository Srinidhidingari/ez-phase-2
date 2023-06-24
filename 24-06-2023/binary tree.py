class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree_ds:
    def __init__(self):
        self.root=None

obj=tree_ds()
n1=Node(100)
n2=Node(200)
obj.root=n1
n3=Node(300)
n1.left=n2
n1.right=n3
n4=Node(400)
n5=Node(500)
n6=Node(600)
n7=Node(700)
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7
print(obj.root.data)
print(n1.right.data)
print(n1.left.data)
print(n2.right.data)
print(n2.left.data)
print(n3.right.data)
print(n3.left.data)

#BST

"""class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree_ds:
    def __init__(self):
        self.root=None

obj=tree_ds()
n1=Node(100)
n2=Node(200)
obj.root=n2
n3=Node(300)
n2.left=n1
n2.right=n3
n4=Node(400)
n5=Node(500)
n6=Node(600)
n7=Node(700)
n3.right=n4
n4.right=n5
n5.right=n6
n6.right=n7
print(obj.root.data)
print(n2.right.data)
print(n2.left.data)
print(n3.right.data)
print(n4.right.data)
print(n5.right.data)
print(n6.right.data)"""





