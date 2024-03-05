class circular_Queue:

    def __init__(self,size):
        self.arr = [None] * size
        self.size = size
        self.front = self.rear = -1
          
    
    def enqueue(self,item):
        #Queue is Full
        if((self.rear+1)%self.size==self.front):
            print("Queue is full")
            return
        #Add to an Empty Queue
        elif(self.front == -1):
            self.front = 0
            self.rear = 0
            self.arr[self.rear] = item
        else:
            self.rear=(self.rear+1)%self.size
            self.arr[self.rear] = item

    def dequeue(self):
        #If queue is Empty
        if(self.front == -1):
            print("Queue is Empty")
            return
        #If there is only one Element
        elif(self.front==self.rear):
            temp = self.arr[self.rear]
            self.rear = -1
            self.front = -1
            return temp
        else:
            temp = self.arr[self.front]
            self.front = (self.front+1)%self.size
            return temp
        
    def peek(self):
        if(self.front == -1):
            print("Queue is Empty")
            return
        else:
            return self.arr[self.front]
        
    # def enqueue_Data_with_Overwrite(self,item):
    #     if((self.rear+1)%self.size==self.front):
    #         self.dequeue()
    #         self.enqueue(item)
    #     else:
    #         self.
        
    def printQueue(self):
        print(self.arr)
        
    
q1 = circular_Queue(3)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.printQueue()
print(q1.peek())
print(q1.dequeue())
q1.enqueue(4)
q1.printQueue()
print(q1.dequeue())
        

    
        
        
    