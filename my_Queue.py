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
q2 = My_Queue()

q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)

q2.enqueue("apple")
q2.enqueue("banana")
q2.enqueue("orange")
q2.enqueue("watermelon")
q2.enqueue("cherry")

print(q1.peek())
print(q2.peek())

print(q1.dequeue())
print(q2.dequeue())

print(q1.peek())
print(q2.peek())

