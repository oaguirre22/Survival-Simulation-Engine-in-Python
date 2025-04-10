class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        nwnode = Node(data)
        
        if not self.front:
            self.front = nwnode
            self.rear = nwnode
            return
        
        self.rear.next = nwnode
        self.rear = nwnode
        
    def dequeue(self):
        if not self.front:
            raise IndentationError("dequeue from empty queue")
        
        removed = self.front
        self.front = self.front.next
        
        if not self.front:
            self.rear = None
            
        return removed.data
    
    def empty(self):
        return not self.front
    
    def peek(self):
        return self.front.data
    
    def size(self):
        s = 0
        actual = self.front
        while actual:
            actual = actual.next
            s += 1
        return s
    
    def __repr__(self):
        output = ""
        actual = self.front
        while actual:
            output += f"{actual.data} -> "
            actual = actual.next
        return output

'''ueue = Queue()

print("-- Metodo Enqueue --")
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)

print("\n -- Metodo peek --")
print("El pico de la cola es: ",  queue.peek())

print("\n -- Metodo empty -- ")
print("La lista esta vacia? ", queue.empty())

print("\n -- Metodo dequeue -- ")
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print("Lista ", queue)

print("\n -- Metodo empty -- ")
print("La lisra esta vacia? ", queue.empty())'''