class Node:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next

class LL:
    def __init__(self,head=None,size=0):
        self.head=head
        self.size=size
        
    def addFirst(self,value):
        nN=Node(value,self.head)
        self.head=nN
        
    def addLast(self,value):
        if self.head==None:
            self.head=Node(value,None)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(value, None)

    def addAtIndex(self,index,value):
        if index == 0:
            self.head=Node(value,None)
        nN=Node(value, None)
        temp=self.head
        for i in range(0,index):
            temp=temp.next
        t=temp.next
        temp.next=nN
        nN.next=t

    def delFirst(self):
        self.head=self.head.next
        
    def len(self):
        self.size=0
        temp=self.head
        while temp!=None:
            self.size+=1
            temp=temp.next
        return self.size
    
    def delAtIndex(self,index):
        count=0
        temp=self.head
        while count!=index:
            temp=temp.next
            count+=1
        temp.next=temp.next.next
    
    def middle(self):
        s=self.head
        f=self.head
        while f!=None:
            f=f.next.next
            s=s.next
        return s.value
    
    def rev(self,temp):
        if temp==None:
            return
        self.rev(temp.next)
        print('%d-->'%(temp.value), end="")

    def reverse(self):
        temp=self.head
        self.rev(temp)
        print('None')

    def display(self):
        temp=self.head
        while temp != None:
            print("%d-->"%(temp.value), end="")
            temp=temp.next
            self.size=+1
        print("None")
    
if __name__=='__main__':
    a=LL()
    a.addFirst(10)
    a.addFirst(20)
    a.addFirst(30)
    a.addFirst(40)
    a.addFirst(50)
    a.addLast(60)
    a.addAtIndex(2,70)
    a.addLast(80)
    a.addAtIndex(4,90)
    a.addFirst(100)
    a.delFirst()
    a.delAtIndex(7)
    a.display()
    print(a.middle())
    a.reverse()