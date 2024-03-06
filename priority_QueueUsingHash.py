import heapq

class Priority_Queue:

    def __init__(self):
        self.arr = []
    
    #insert at its corresponding position acc to priority in queue
    def enqueue(self, item, priority):
        newItem = (priority, item)
        heapq.heappush(self.arr, newItem)
    
    #dequeue the element with highest priority
    def dequeue(self):
        if len(self.arr) == 0:
            print("Queue is Empty")
        else:
            return heapq.heappop(self.arr)

    #peek the element with highest priority   
    def peek(self):
        if len(self.arr) == 0:
            print("Queue is Empty")
        else:
            return self.arr[0]
    
    def print_Queue_basedOn_Priority(self):
        temp = self.arr.copy()
        while len(temp)!= 0:
            print(heapq.heappop(temp))

q1 = Priority_Queue()
q1.enqueue('Make coffee', 4)
q1.enqueue('Make Tea', 2)
q1.enqueue('Study', 1)
q1.enqueue('Sing', 3)

print()

print("Peek the queue:")
print(q1.peek())

print("\nInitial queue based on priority")
q1.print_Queue_basedOn_Priority()

print("\nDeque Element:")
print(q1.dequeue())


print("\nQueue after Dequeue:")
q1.print_Queue_basedOn_Priority()




