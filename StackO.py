
class StackO:
    def __init__(self):
        self.items = []  # Inicializa una lista vacía para el Stack
        
    def push(self, data):
        self.items.append(data)  # Agrega un elemento al Stack
    
    def pop(self):
        if self.items == []:  # Verifica si el Stack está vacío antes de hacer pop
            raise Exception("Underflow")  # Levanta una excepción si el Stack está vacío
        
        return self.items.pop()  # Elimina y devuelve el último elemento del Stack
    
    def peek(self):
        if self.items == []:  # Verifica si el Stack está vacío antes de hacer peek
            raise Exception("Underflow")  # Levanta una excepción si el Stack está vacío
            
        return self.items[-1]  # Devuelve el último elemento del Stack sin eliminarlo
    
    def length(self):
        return len(self.items)  # Devuelve la longitud del Stack
    
    def print_stack(self):
        print(self.items)  # Imprime el contenido del Stack

# Implementación de Stack utilizando nodos
class Node:
    def __init__(self, data=None):
        self.data = data  # Valor del nodo
        self.next = None  # Puntero al siguiente nodo
    
class Stack:
    def __init__(self):
        self.top = None  # Puntero al nodo superior del Stack
        
    def push(self, data):
        new_node = Node(data)  # Crea un nuevo nodo con los datos proporcionados
        new_node.next = self.top  # Enlaza el nuevo nodo al Stack existente
        self.top = new_node  # Actualiza el puntero top al nuevo nodo
    
    def pop(self):
        if not self.top:  # Verifica si el Stack está vacío antes de hacer pop
            raise Exception("Underflow")  # Levanta una excepción si el Stack está vacío
        
        propped = self.top  # Almacena los datos del nodo superior
        self.top = self.top.next  # Mueve el puntero top al siguiente nodo
        
        return propped.data  # Devuelve los datos eliminados del Stack
    
    def peek(self):
        if not self.top:  # Verifica si el Stack está vacío antes de hacer peek
            raise Exception("Underflow")  # Levanta una excepción si el Stack está vacío
            
        return self.top.data  # Devuelve los datos del nodo superior sin eliminarlo
    
    def length(self):
        current = self.top
        counter = 0
        while current:
            current = current.next
            counter += 1
            
        return counter  # Corrige la indentación para devolver el valor correcto
     
    def is_empty(self):
        if not self.top:
            return True
        else:
            return False
            
    def print_stack(self):
        current = self.top
        while current:
            print(current.data, end=", ")
            current = current.next
            
        print()  # Salto de línea al final de la impresión
        

if __name__ ==  "__main__":
    
    """ 
    Lista built-in de Python como Stack
    """
    lista = []
    lista.append(11)
    lista.append(33)
    lista.append(22)
    print(lista)
    
    valor = lista.pop() #Elimina el ultimo elemento y lo retorna como una pila
    print(valor)
    print(lista) 
    valor2 = lista[-1] #Obtener ultimo elemento sin eliminarlo
    print(valor2)
    print(lista) 
    print()
    
    
    """ 
    Lista built-in de Python con blindaje para Stack
    """
            
    s_py = StackO()
    
    s_py.push(11)
    s_py.push(22)
    s_py.push(33)
    
    s_py.print_stack()
    
    print(s_py.length(), s_py.peek(), s_py.pop())
    s_py.print_stack()
    
    
    """
    Stack con Listas Enlazadas
    """
    
    s = Stack()
    
    s.push(11)
    s.push(22)
    s.push(33)
    
    s.print_stack()
        
        
