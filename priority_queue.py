class Priority_Queue:

    def __init__(self):
        self.arr = []

    def enqueue(self, item, priority):
        newItem = {
            'item': item,
            'priority': priority
        }
        if not self.arr:
            self.arr.append(newItem)
        elif self.arr[0]['priority'] > priority:
            self.arr.insert(0, newItem)
        elif self.arr[-1]['priority'] < priority:
            self.arr.append(newItem)
        else:
            i = 0
            while i < len(self.arr):
                if self.arr[i]['priority'] < priority and self.arr[i + 1]['priority'] > priority:
                    self.arr.insert(i + 1, newItem)
                    break
                i += 1

    def dequeue(self):
        if len(self.arr) == 0:
            print("Queue is Empty")
        else:
            return self.arr.pop(0)

    def peek(self):
        if len(self.arr) == 0:
            print("Queue is Empty")
        else:
            return self.arr[0]

    def print_Queue_basedOn_Priority(self):
        for item in self.arr:
            print(item)


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
