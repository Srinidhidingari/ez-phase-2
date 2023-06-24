queue=[]
def enqueue():
    if len(queue)==n:
        print("queue is full")
    else:
        element=input("enter a no:")
        queue.append(element)
        print(queue)
def dequeue():
    if not queue:
        print("queue is empty add an element:")
    else:
        d=queue.pop(0)
        print(d,"removed")
        print(queue)
def display():
    if len(queue)==0:
        print("queue is empty")
    else:
        print(queue)
    
n=int(input("enter the size of queue:"))      
while True:
    print("select an option: 1.enqueue 2.dequeue 3.display 4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("enter correct choice:")    
    
