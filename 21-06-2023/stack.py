st=[]
def push_element():
    if len(st)==n:
        print("stack is full")
    else:
        element=input("enter a no:")
        st.append(element)
        print(st)
def pop_element():
    if not st:
        print("stack is empty add an element:")
    else:
        d=st.pop()
        print(d,"removed")
        print(st)
def display():
    if len(st)==0:
        print("stack is empty")
    else:
        print(st)
    
n=int(input("enter the size of stack:"))      
while True:
    print("select an option: 1.push 2.pop 3.display 4.quit")
    choice=int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("enter correct choice:")    
    
