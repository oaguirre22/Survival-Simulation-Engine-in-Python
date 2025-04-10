
import time
from StackO import Stack
from ColaDePrioridad import PQueueAP
from Colas import Queue
from DoubleEndedQueue import MyDeque
import random 

#class principal
class ciudadano:
    def __init__(self, nombre, clase):
        self.nombre = nombre
        self.clase = clase
        self.posicion = (0,0)
        self.color = (255, 255, 255)
class recolector:
    def __init__(self, nombre, clase):
        self.nombre = nombre
        self.clase = clase
        self.posicion = (0, 0)
        self.color = (0, 255, 0)  # Color genérico para recolectores

class guerrero:
    def __init__(self, nombre, clase):
        self.nombre = nombre
        self.clase = clase
        self.posicion = (0,0) 
        self.color = (255, 0, 0)

class profeta:
    def __init__(self, nombre = 'Curandero', clase = 'Profeta'):
        self.nombre = nombre
        self.clase = clase
        self.posicion = (0,0)
        self.color = (128, 0, 128)

       
        
#subclases: Guerreros(Soldado, Jinete, pillager), ciudadano(Constructor, Carpintero, Bufon), Recolectores(Leñador, Minero), Profetas(Curandero)
class constructor(ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre,'constructor')
        self.color = (128, 128, 0) 

class carpintero(ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre,'carpintero' )
        self.color = (0, 128, 255)

class bufon(ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre,'Bufon')
        self.color = (255, 0, 255)

class soldado(guerrero):
    def __init__(self, nombre,):
        super().__init__(nombre,'soldado')
        self.color = (255, 0, 0)

class pillager(guerrero):
    def __init__(self, nombre):
        super().__init__(nombre,'pillager')
        self.color = (255, 128, 0)


class jinete(guerrero):
    def __init__(self, nombre,):
        super().__init__(nombre,'jinete')
        self.color = (0, 255, 128)

class leñador(recolector):
    def __init__(self,nombre):
        super().__init__(nombre, 'leñador')
        self.color = (0, 128, 0) 

class minero(recolector):
    def __init__(self,nombre):
        super().__init__(nombre, 'minero')
        self.color = (128, 128, 128)

 
 # Edificios por def       
class centro_de_recoleccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ciudadanos = 0
        self.construcciones = 0

