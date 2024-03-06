class My_Queue:

    def __init__(self):
        self.arr = []
    
    def enqueue(self,item):
        self.arr.append(item)

    def dequeue(self):
        if(len(self.arr) == 0):
            print("Queue is Empty")
        else:
            return self.arr.pop(0)
        
    def peek(self):
        if(len(self.arr) == 0):
            print("Queue is Empty")
        else:
            return self.arr[0]
    



q1 = My_Queue()

print()

print("Trying to deque and peek empty queue:")
q1.dequeue()
q1.peek()


q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)

print("\nPeek the queue after adding elements:")
print(q1.peek())

print("\nDequeue the queue:")
print(q1.dequeue())

print("\nPeek after dequeue:")
print(q1.peek())

