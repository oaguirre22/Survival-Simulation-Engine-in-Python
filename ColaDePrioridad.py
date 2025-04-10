import random
class PQueueSimplest:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
        self.queue.sort()
        
    def dequeue(self):
        if not self.queue:
            raise IndexError("Dequeue from empty queue")
        
        return self.queue.pop(0)
    
    def peek(self):
        if not self.queue:
            raise IndexError("Dequeue from empty queue")
        
        return self.queue[0]
    
    def lenght(self):
        return len(self.queue)
    
    def empty(self):
        return not self.queue
    
    def __repr__(self):
        return f"{self.queue}"
    
class PQueueAP:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, priority):
        self.queue.append((priority)) 
        
        self.queue.sort(key=lambda x: x[0])
    
    def dequeue(self):
        if not self.queue:
            raise IndexError("Dequeue from empty queue")
        
        priority = self.queue.pop(0)
        return priority
    
    
    def peek(self):
        if not self.queue:
            raise IndexError("Dequeue from empty queue")
        return self.queue[0][0], self.queue[0][1]
    
    def lenght(self):
        return len(self.queue)
    
    def empty(self):
        return not self.queue
    
    def __repr__(self):
        return f"{self.queue}"

class cliente:
    def __init__(self, name, lastname, age, phone, email):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"{self.lastname}, {self.name}, {self.age}, {self.email}"
    
class PQueueSC:
    def __init__(self):
        self.queue = []
    
    def enqueue (self, cliente):
        self.queue.append(cliente)
        self.queue.sort(key = lambda cliente: cliente.age)
    
    def print_queue(self):
        for i in self.queue:
            print(i)
    
    
    
    
if __name__ == "__main__":
    '''qsimple = PQueueSimplest()
    for i in range(10):
        qsimple.enqueue(random.randint(10, 99))
        
    print(qsimple)
    
    qsimplekey = PQueueAP()
    for i in range(10):
        qsimplekey.enqueue(random.randint(1, 10), random.randint(10, 99))
        
    print(qsimplekey)
    
    cliente1 = cliente("Oscar", "Aguirre", 21, 4491556243, "elpajas@hotmail")
    cliente2 = cliente("Julio", "Serna", 20, 4491720741, "papiking@hotmail")
    cliente3 = cliente("Ricardo", "Villanueva", 20, 4493862976, "villavicios@hotmail")
    cliente4 = cliente("Gerardo", "Macias", 22, 4498057611, "elhorny@hotmail")
    
    pq = PQueueSC()
    pq.enqueue(cliente1)
    pq.enqueue(cliente2)
    pq.enqueue(cliente3)
    pq.enqueue(cliente4)

    pq.print_queue()'''