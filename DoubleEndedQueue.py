class Nodo:
    def __init__(self, valor):
        self.valor = valor  # Almacena el valor del nodo
        self.siguiente = None  # Puntero al siguiente nodo
        self.anterior = None  # Puntero al nodo anterior

class MyDeque:
    def __init__(self):
        self.frente = None  # Puntero al nodo frontal
        self.rear = None    # Puntero al nodo trasero

    def insertFront(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.frente is None:  # Si la deque está vacía
            self.frente = nuevo_nodo
            self.rear = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.frente
            self.frente.anterior = nuevo_nodo
            self.frente = nuevo_nodo

    def insertRear(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.rear is None:  # Si la deque está vacía
            self.frente = nuevo_nodo
            self.rear = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.rear
            self.rear.siguiente = nuevo_nodo
            self.rear = nuevo_nodo

    def removeLeft(self):
        if self.frente is None:  # Si la deque está vacía
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is not None:  # Si hay más nodos
            self.frente.anterior = None
        else:  # Si se eliminó el último nodo
            self.rear = None
        return valor

    def removeRight(self):
        if self.rear is None:  # Si la deque está vacía
            return None
        valor = self.rear.valor
        self.rear = self.rear.anterior
        if self.rear is not None:  # Si hay más nodos
            self.rear.siguiente = None
        else:  # Si se eliminó el último nodo
            self.frente = None
        return valor

    def remove(self, valor):
        if self.frente is None:  # Si la deque está vacía
            return None

        # Caso 1: Eliminar el nodo frontal
        if self.frente.valor == valor:
            return self.removeLeft()

        # Caso 2: Eliminar el nodo trasero
        if self.rear.valor == valor:
            return self.removeRight()

        # Caso 3: Eliminar un nodo intermedio
        nodo_actual = self.frente.siguiente  # Comienza desde el segundo nodo
        while nodo_actual is not None:
            if nodo_actual.valor == valor:
                # Ajustar los punteros de los nodos anterior y siguiente
                if nodo_actual.anterior is not None:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                if nodo_actual.siguiente is not None:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                return valor  # Devuelve el valor eliminado
            nodo_actual = nodo_actual.siguiente
        
        return None  # Si no se encuentra el valor

    def isEmpty(self):
        return self.frente is None

    def peekFront(self):
        return self.frente.valor if self.frente else None

    def peekRear(self):
        return self.rear.valor if self.rear else None

    def merge_into(deque1, deque2):
        if deque2.isEmpty():  # Si deque2 está vacía, no hay nada que añadir
            return deque1

        if deque1.isEmpty():  # Si deque1 está vacía, simplemente asigna deque2 a deque1
            deque1.frente = deque2.frente
            deque1.rear = deque2.rear
        else:
            # Conectar el rear de deque1 con el frente de deque2
            deque1.rear.siguiente = deque2.frente
            deque2.frente.anterior = deque1.rear
            deque1.rear = deque2.rear  # Actualizar el rear de deque1

        # Vaciar deque2 (opcional, si ya no quieres usar deque2 después)
        deque2.frente = None
        deque2.rear = None

        return deque1


    def __iter__(self):
        self._current = self.frente  # Inicializa el nodo actual en el frontal
        return self  # Devuelve el mismo objeto como iterador

    def __next__(self):
        if self._current is not None:
            valor = self._current.valor  # Guarda el valor actual
            self._current = self._current.siguiente  # Avanza al siguiente nodo
            return valor  # Retorna el valor
        else:
            raise StopIteration  # Lanza StopIteration cuando se acaben los elementos
