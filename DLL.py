
class Node:
    def __init__(self,value=None,next=None,prev=None):
        self.value=value
        self.next=next
        self.prev=prev

class DLL:
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
    
    def addFirst(self,value):
        nN=Node(value)
        nN.next=self.head
        if(self.head!=None):
            self.head.prev=nN
        if(self.tail==None):
            self.tail=self.head
        self.head=nN
    
    def addLast(self,value):
        if self.tail==None:
            self.addFirst(value)
        else:
            nN=Node(value)
            self.tail.next=nN
            nN.prev=self.tail
            self.tail=nN

    def addAtIndex(self,index,value):
        if(index==0):
            self.addFirst(value)
        if(index==self.len()):
            self.addLast
        nN=Node(value)
        temp=self.head
        for i in range(0,index):
            temp=temp.next
        t=temp.next
        temp.next=nN
        nN.prev=temp
        nN.next=t

    def delFirst(self):
        if(self.head.next==None):
            tail=None
        self.head=self.head.next

    def delLast(self):
        if self.head.next==None:
            self.head=None
            self.tail=None
        temp=self.head
        for i in range(1,self.len()-1):
            temp=temp.next
        temp.next=None
        self.tail=temp

    def delAtIndex(self,index):
        count=0
        temp=self.head
        while count!=index:
            temp=temp.next
            count+=1
        temp.next=temp.next.next

    def revDLL(self,temp):
        if(temp==None):
            return
        self.revDLL(temp.next)
        print("%d-->"%(temp.value),end="")

    def reverse(self):
        temp=self.head
        self.revDLL(temp)
    
    def len(self):
        temp=self.head
        size=0
        while temp!=None:
            temp=temp.next
            size+=1
        return size
    
    def display(self):
        temp=self.head
        while temp!=None:
            print("%d-->"%(temp.value),end="")
            temp=temp.next
    
if __name__=='__main__':
    a=DLL()
    a.addFirst(10)
    a.addFirst(20)
    a.addFirst(30)
    a.addLast(40)
    a.addLast(50)
    a.delFirst()
    a.addFirst(5)
    a.addFirst(15)
    a.display()
    print()
    a.delLast()
    a.delLast()
    a.display()
    print()
    a.reverse()