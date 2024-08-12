class queue:
    def __init__(self):
        self.item = []
    def is_empty(self):
        return len(self.item)==0
    def enqueue(self,data):
        self.item.append(data)
    def dequeue (self):
        if not self.is_empty():
          self.item.pop(0)
        else:
            raise IndexError("queue underflow")
    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError("queue underflow")
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("queue underflow")
    def size(self):
        if not self.is_empty():
            return len(self.item)
        else:
            raise IndexError("len = 0")

q1 = queue()
try:
    print(q1.get_front()) #exception case handell
except IndexError as e:
    print(e.args[0])
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
print("front=",q1.get_front(),"rear=",q1.get_rear())
try:
    q1.dequeue()
    print("size is =",q1.size())
    print(q1.dequeue()) #exception case handell
except IndexError as e:
    print(e.args[0])


        
    
    

