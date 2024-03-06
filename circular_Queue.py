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
            # self.arr[self.rear] = None
            self.rear = -1
            self.front = -1
            return temp
        else:
            temp = self.arr[self.front]
            # self.arr[self.front] = None
            self.front = (self.front+1)%self.size
            return temp
        
    def peek(self):
        if(self.front == -1):
            print("Queue is Empty")
            return
        else:
            return self.arr[self.front]
        
    def enqueue_Data_with_Overwrite(self,item):
        #If queue is empty
        if(self.front == -1):
            self.front = 0
            self.rear = 0
            self.arr[self.rear] = item
        else:
            self.rear=(self.rear+1)%self.size
            self.arr[self.rear] = item
            if self.rear == self.front:
                self.front = (self.front + 1) % self.size
        
    def printQueue(self):
        print(self.arr)
        
    
q1 = circular_Queue(5)

print()
print("Initial queue with size: 5")
q1.enqueue("Apple")
q1.enqueue("Mango")
q1.enqueue("Cherry")
q1.enqueue("Banana")
q1.enqueue("Grapes")

print("\nTrying to enqueue when queue is full:")
q1.enqueue("Orange")

print("\nQueue Status:")
q1.printQueue()

print("\nAdding an element to overwrite the previous data when full.")
q1.enqueue_Data_with_Overwrite("Strawberry")
q1.enqueue_Data_with_Overwrite("Papaya")

        
print("\nQueue Status now:")
q1.printQueue()
    
print("\nDequeue an element:")
print(q1.dequeue())
