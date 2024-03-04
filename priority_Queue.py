class Priority_Queue:

    def __init__(self):
        self.arr = []
    
    def enqueue(self,item,priority):
        newItem = {
            'item' : item,
            'priority' : priority
        }
        self.arr.append(newItem)

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
    
    def print_Queue_basedOn_Priority(self):
        sorted_Arr = self.arr.sort(True,key = lambda x:x['priority'])
        print(sorted_Arr)
        
    