from Ascii import animacion_pueblo, animacion_aldeano_cazando, animacion_aldeano_picando, animacion_construccion_casa
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
    
cola_prioridad = PQueueAP()    
def MenuAcciones(acciones):
    MAX_ACCIONES = 5  # Constante para el máximo de acciones permitidas
    animacion_pueblo()
    while True:
        print("\n-- Menu de Acciones --")
        print(f"Acciones en cola: {acciones.size()}/{MAX_ACCIONES}")
        print("1.- Farmear")
        print("2.- Construir")
        print("3.- Cazar")
        print("4.- Resguardarse")
        print("5.- Atacar")
        print("6.- Nuevo personaje Recolector")
        print("7.- Realizar acciones")
        
        opcion = input("\nSelecciona una opcion del 1 - 7: ")
        
        # Si ya alcanzamos el máximo de acciones, solo permitir ejecutar o salir
        if acciones.size() >= MAX_ACCIONES and opcion not in ['7']:
            print(f"\nNo puedes agregar más tareas. La cola está llena ({MAX_ACCIONES}/{MAX_ACCIONES})")
            print("Por favor, ejecuta las acciones actuales (opción 7)")
            continue
            
        if opcion == '1':
            print("\nHaz seleccionado la opcion de Farmear")
            acciones.enqueue("Farmear")
        elif opcion == '2':
            print("\nHaz seleccionado la opcion de Construir nuevo edificio")
            acciones.enqueue("Construir")
        elif opcion == '3':
            print("\nHaz seleccionado la opcion de Cazar")
            acciones.enqueue("Cazar")
        elif opcion == '4':
            print("\nHaz seleccionado la opcion de Resguardarse")
            acciones.enqueue("Resguardarse")
        elif opcion == '5':
            print("\nHaz seleccionado la opcion de Atacar")
            acciones.enqueue("Atacar")
        elif opcion == '6':
            print("\nHaz seleccionado la opcion de Crear nuevo personaje Recolector")
            acciones.enqueue("Crear nuevo personaje Recolector")
        elif opcion == '7':
            if acciones.empty():
                print("\nNo hay acciones para realizar")
                continue
            print("\nRealizando acciones...")
            RealizarAccion(acciones, personajesDisponibles)
        else:
            print("\nOpcion no válida, por favor selecciona una opcion del 1 - 7")

def RealizarAccion(acciones, personajesDisponibles):
    if acciones.empty():
        print("No hay acciones en espera")
        return
    
    acciones_no_realizadas = Queue()
    
    while not acciones.empty():
        accion = acciones.dequeue()
        if accion == "Crear nuevo personaje Recolector":
            centro.crear_personaje_recolector()  # Llamar directamente a la función de creación
            continue
        mejorPersonaje = None
        mejorCompatibilidad = -1
        
        if personajesDisponibles.isEmpty():
            print(f"No hay personajes disponibles para realizar la acción: {accion}")
            acciones_no_realizadas.enqueue(accion)
            continue
        
        # Lista temporal para almacenar personajes mientras buscamos
        personajes_temp = []
        
        # Buscar el mejor personaje disponible
        while not personajesDisponibles.isEmpty():
            personaje = personajesDisponibles.removeLeft()
            personajes_temp.append(personaje)
            compat = compatibilidad(personaje, accion)
            if compat is not None and compat > mejorCompatibilidad:
                mejorPersonaje = personaje
                mejorCompatibilidad = compat
        
        # Restaurar todos los personajes excepto el seleccionado
        for personaje in personajes_temp:
            if personaje != mejorPersonaje:
                personajesDisponibles.insertRear(personaje)
        
        if mejorPersonaje:
            # Asignar prioridad a la acción
            prioridades = {
                "Crear nuevo personaje Recolector": 1,
                "Atacar": 2,
                "Resguardarse": 3,
                "Construir": 4,
                "Farmear": 5,
                "Cazar": 6
            }
            prioridad = prioridades.get(accion, 6)
            
            # Agregar a la cola de prioridad
            cola_prioridad.enqueue((prioridad, accion, mejorPersonaje))
            print(f"{mejorPersonaje.nombre} ha sido asignado para {accion}")
        else:
            print(f"No se encontró personaje adecuado para la acción: {accion}")
            acciones_no_realizadas.enqueue(accion)
    # Procesar la cola de prioridad
    ejecutar_cola_prioridad()
    raid_prob.Raid()

    
    # Devolver las acciones no realizadas a la cola original
    while not acciones_no_realizadas.empty():
        acciones.enqueue(acciones_no_realizadas.dequeue())
    
    # Devolver las acciones no realizadas a la cola original
    while not acciones_no_realizadas.empty():
        acciones.enqueue(acciones_no_realizadas.dequeue())
            
# Función para ejecutar las acciones de la cola de prioridad
def ejecutar_cola_prioridad():
    while not cola_prioridad.empty():
        # Ejecutamos la tarea con mayor prioridad
        prioridad, accion, personaje = cola_prioridad.dequeue()
        print(f"\nEjecutando {accion} con {personaje.nombre} (Prioridad: {prioridad})")
        
        # Simulación de la acción
        if accion == "Construir":
            
            print(f"{personaje.nombre} está construyendo...")
            print("Que tipo de construccion quieres?")
            print("1.- Casa")
            print("2.- Almacen")
            construccion_op = input("Selecciona un tipo de construccion: ")
            if construccion_op == "1":
                print("Haz seleccionado construir una casa.")
                animacion_construccion_casa()
                recursos.construccion_casa()
            elif construccion_op == "2":
                print("Haz seleccionado construir un almacen.")
                recursos.construccion_almacen()
            time.sleep(2)
        elif accion == "Farmear":
            animacion_aldeano_picando()
            print(f"{personaje.nombre} ({personaje.clase}) está farmeando...")
            
            time.sleep(2)
            recursos.recolectar(personaje, accion)
            time.sleep(2)
        elif accion == "Cazar":
            animacion_aldeano_cazando()
            print(f"{personaje.nombre} está cazando...")
            time.sleep(2)
            recursos.recolectar(personaje, accion)
            time.sleep(2)
        elif accion == "Resguardarse":
            print(f"{personaje.nombre} está resguardándose...")
            time.sleep(2)
        elif accion == "Atacar":
            print(f"{personaje.nombre} está atacando...")
            time.sleep(2)
            recursos.recolectar(personaje, accion)
            time.sleep(2)

        # Después de realizar la acción, volver a agregar el personaje a personajesDisponibles
        print(f"{personaje.nombre} ha terminado su tarea y está disponible nuevamente.")
        personajesDisponibles.insertRear(personaje)

        # Mostrar las tareas pendientes después de ejecutar la acción
        if not cola_prioridad.empty():
            print("\n-- Tareas pendientes después de ejecutar --")
            mostrar_acciones_prioridad(cola_prioridad)

# Función para mostrar las acciones en la cola de prioridad
def mostrar_acciones_prioridad(cola_prioridad):
    if cola_prioridad.empty():
        print("No hay acciones en espera")
        MenuAcciones(acciones)
    else:
        for i, (prioridad, accion, personaje) in enumerate(cola_prioridad.queue, 1):
            print(f"{i}. Acción: {accion}, Personaje: {personaje.nombre}, Prioridad: {prioridad}")

# Compatibilidad
def compatibilidad( personaje, accion):
    if accion == 'Atacar':
        if isinstance(personaje, soldado):
            return 2.0
        elif isinstance(personaje, jinete):
            return 2.0
        elif isinstance(personaje, leñador):
            return 0.8
        elif isinstance(personaje, minero):
            return 0.7
        elif isinstance(personaje, constructor):
            return 0.6
        elif isinstance(personaje, carpintero):
            return 0.5
        elif isinstance(personaje, bufon):
            return 0.4
        elif isinstance(personaje, profeta):
            return 0.1
        
        
    elif accion == "Farmear":
        if isinstance(personaje, minero):
            return 1.0
        elif isinstance(personaje, leñador):
            return 1.0
        elif isinstance(personaje, soldado):
            return 0.8
        elif isinstance(personaje, jinete):
            return 0.8
        elif isinstance(personaje, carpintero):
            return 0.6
        elif isinstance(personaje, constructor):
            return 0.5
        elif isinstance(personaje, bufon):
            return 0.4
        elif isinstance(personaje, profeta):
            return 0.4
        
    elif accion == 'Construir':
        if isinstance(personaje, constructor):
            return 1.0
        elif isinstance(personaje, carpintero):
            return 1.0
        elif isinstance(personaje, leñador):
            return 0.8
        elif isinstance(personaje, minero):
            return 0.7
        elif isinstance(personaje, soldado):
            return 0.6
        elif isinstance(personaje, jinete):
            return 0.5
        elif isinstance(personaje, bufon):
            return 0.4
        elif isinstance(personaje, profeta):
            return 0.4
    
    elif accion == 'Resguardarse':
        if isinstance(personaje, constructor):
            return 1.0
        elif isinstance(personaje, carpintero):
            return 1.0
        elif isinstance(personaje, leñador):
            return 1.0
        elif isinstance(personaje, minero):
            return 1.0
        elif isinstance(personaje, soldado):
            return 1.0
        elif isinstance(personaje, jinete):
            return 1.0
        elif isinstance(personaje, bufon):
            return 1.0
        elif isinstance(personaje, profeta):
            return 1.0
    elif accion == 'Cazar':
        if isinstance(personaje, soldado):
            return 2.0
        elif isinstance(personaje, jinete):
            return 2.0
        elif isinstance(personaje, leñador):
            return 1.0
        elif isinstance(personaje, minero):
            return 0.8
        elif isinstance(personaje, constructor):
            return 0.6
        elif isinstance(personaje, carpintero):
            return 0.5
        elif isinstance(personaje, bufon):
            return 0.1
        elif isinstance(personaje, profeta):
            return 0.1
        

class Recursos:
    def __init__(self):
        self.madera = 100
        self.minerales = 0
        self.piedra = 100
        self.carne = 20
        self.moneda = 100
        self.casas = 2
        self.almacenes = 1

    def recolectar(self, personaje, accion):
        # Asignar la cantidad de recursos según compatibilidad
        compat = compatibilidad(personaje, accion)
        cantidad = int(random.randint(30, 50) * compat)  # Generar recursos basado en compatibilidad
        cantidad2 = int(random.randint(5, 20) * compat)
        if compat:
            if accion == "Farmear":
                print("Que tipo de recurso quieres farmear?")
                print("1.- Madera")
                print("2.- Piedra")
                recurso_op = input("Selecciona un recurso: ")
                if recurso_op == "1":
                    print("Haz seleccionado recolectar madera.")
                    if isinstance(personaje, leñador):
                        new_cantidad = cantidad*2
                        self.madera += new_cantidad
                        print(f"{personaje.nombre} ha recolectado {new_cantidad} de madera.")
                    elif isinstance(personaje, minero):
                        self.madera += cantidad
                        print(f"{personaje.nombre} ha recolectado {cantidad} de madera.")
                    elif isinstance(personaje, soldado):
                        self.madera += cantidad
                        print(f"{personaje.nombre} ha recolectado {cantidad} de madera.")
                    elif isinstance(personaje, jinete):
                        self.madera += cantidad
                        print(f"{personaje.nombre} ha recolectado {cantidad} de madera.")
                    elif isinstance(personaje, carpintero):
                        self.madera += cantidad
                        print(f"{personaje.nombre} ha recolectado {cantidad} de madera.")
                    elif isinstance(personaje, constructor):
                        self.madera += cantidad
                        print(f"{personaje.nombre} ha recolectado {cantidad} de madera.")
                    elif isinstance(personaje, bufon):
                        self.madera += cantidad
                        print(f"{personaje.nombre} ha recolectado {cantidad} de madera.")
                    elif isinstance(personaje, profeta):
                        self.madera += cantidad
                        print(f"{personaje.nombre} ha recolectado {cantidad} de madera.")
                elif recurso_op == "2":
                    print("Haz seleccionado recolectar piedra.")
                    if isinstance(personaje, minero):
                        new_cantidad = cantidad*2
                        self.piedra += new_cantidad
                        self.minerales += cantidad2
                        print(f"{personaje.nombre} ha recolectado {new_cantidad} de piedra y {cantidad2} minerales.")
                    elif isinstance(personaje, leñador):
                        self.piedra += cantidad
                        print(f"{personaje.nombre} ha recolectado {cantidad} de piedra.")
                    elif isinstance(personaje, soldado):
                        self.piedra += cantidad
                        print(f"{personaje.nombre} ha recolectado {cantidad} de piedra.")
                    elif isinstance(personaje, jinete):
                        self.piedra += cantidad
                        print(f"{personaje.nombre} ha recolectado {cantidad} de piedra.")
                    elif isinstance(personaje, carpintero):
                        self.piedra += cantidad
                        print(f"{personaje.nombre} ha recolectado {cantidad} de piedra.")
                    elif isinstance(personaje, constructor):
                        self.piedra += cantidad
                        print(f"{personaje.nombre} ha recolectado {cantidad} de piedra.")
                    elif isinstance(personaje, bufon):
                        self.piedra += cantidad
                        print(f"{personaje.nombre} ha recolectado {cantidad} de piedra.")
                    elif isinstance(personaje, profeta):
                        self.piedra += cantidad
                        print(f"{personaje.nombre} ha recolectado {cantidad} de piedra.")
            if accion == "Cazar":
                if isinstance(personaje, soldado):
                    self.carne += cantidad
                    print(f"{personaje.nombre} ha recolectado {cantidad} de carne.")
                elif isinstance(personaje, jinete):
                    self.carne += cantidad
                    print(f"{personaje.nombre} ha recolectado {cantidad} carne.")
                elif isinstance(personaje, leñador):
                    self.carne += cantidad
                    print(f"{personaje.nombre} ha recolectado {cantidad} de carne.")
                elif isinstance(personaje, minero):
                    self.carne += cantidad
                    print(f"{personaje.nombre} ha recolectado {cantidad} de carne.")
                elif isinstance(personaje, carpintero):
                    self.carne += cantidad
                    print(f"{personaje.nombre} ha recolectado {cantidad} de carne.")
                elif isinstance(personaje, constructor):
                    self.carne += cantidad
                    print(f"{personaje.nombre} ha recolectado {cantidad} de carne.")
                elif isinstance(personaje, bufon):
                    self.moneda += cantidad
                    print(f"{personaje.nombre} ha recolectado {cantidad} de monedas.")
                elif isinstance(personaje, profeta):
                    self.monedas += cantidad
                    print(f"{personaje.nombre} ha recaudado {cantidad} de monedas.")
            if accion == "Atacar":
                if isinstance(personaje, soldado):
                    self.moneda += cantidad
                    print(f"{personaje.nombre} ha atacado una aldea cercana y consiguio {cantidad} de monedas.")
                elif isinstance(personaje, jinete):
                    self.moneda += cantidad
                    print(f"{personaje.nombre} ha atacado una aldea cercana y consiguio {cantidad} de monedas.")
                elif isinstance(personaje, leñador):
                    self.moneda += cantidad
                    print(f"{personaje.nombre} ha atacado una aldea cercana y consiguio {cantidad} de monedas.")
                elif isinstance(personaje, minero):
                    self.moneda += cantidad
                    print(f"{personaje.nombre} ha atacado una aldea cercana y consiguio {cantidad} de monedas.")
                elif isinstance(personaje, carpintero):
                    self.moneda += cantidad
                    print(f"{personaje.nombre} ha atacado una aldea cercana y consiguio {cantidad} de monedas.")
                elif isinstance(personaje, constructor):
                    self.moneda += cantidad
                    print(f"{personaje.nombre} ha atacado una aldea cercana y consiguio {cantidad} de monedas.")
                elif isinstance(personaje, bufon):
                    print(f"{personaje.nombre} no tiene ni el valor ni la fuerza de atacar.")
                elif isinstance(personaje, profeta):
                    print(f"{personaje.nombre} prefirio seguir sus principios y no ataco.")
    def construccion_casa(self):
        if self.madera < 50:
            print(f"No tienes la madera suficiente para construir una casa. Te faltan {50 - self.madera} unidades.")
        elif self.piedra < 50:
            print(f"No tienes la piedra suficiente para construir una casa.Te faltan {50 - self.piedra} unidades.")
        elif self.moneda < 25:
            print(f"No tienes las monedas suficientes para construir una casa.Te faltan {25 - self.moneda} unidades.")
        else:
            print("Construyendo casa...")
            self.madera -= 50
            self.piedra -= 50
            self.moneda -= 25
            self.casas += 1
            print(f"Casa construida. Total casas: {self.casas}")
    def construccion_almacen(self):
        if self.madera < 70:
            print(f"No tienes la madera suficiente para construir un almacen.Te faltan {70 - self.madera} unidades.")
        elif self.piedra < 70:
            print(f"No tienes la piedra suficiente para construir un almacen. Te faltan {70 - self.piedra} unidades.")
        elif self.moneda < 35:
            print(f"No tienes las monedas suficientes para construir un almacen. Te faltan {35 - self.moneda} unidades.")
        else:
            print("Construyendo almacen...")
            self.madera -= 70
            self.piedra -= 70
            self.moneda -= 35
            self.almacenes += 1

class centro_de_recoleccion:
    def __init__(self):
        self.ciudadanos = 4
        self.recursos = recursos
    def crear_personaje_recolector(self):
        if  self.ciudadanos >= ((self.recursos.casas) * 4):
            print("No tienes suficientes casas para generar mas personajes")
        else:
            if self.recursos.carne > 30:  # Si tienes recursos suficientes
                print("Selecciona la clase del nuevo personaje: Leñador, Minero, Carpintero, Constructor, Bufon o Profeta.")
                clase = input("Clase: ").strip().lower()  # Input para clase y pasamos a minúsculas para evitar errores

                if clase == "leñador":
                    print("¿Qué nombre tendrá el nuevo Leñador?")
                    nombre = input("Nombre: ").strip()
                    nuevo_personaje = leñador(nombre)
                    self.ciudadanos += 1
                elif clase == "minero":
                    print("¿Qué nombre tendrá el nuevo Minero?")
                    nombre = input("Nombre: ").strip()
                    nuevo_personaje = minero(nombre)
                    self.ciudadanos += 1
                elif clase == "carpintero":
                    print("¿Qué nombre tendrá el nuevo Carpintero?")
                    nombre = input("Nombre: ").strip()
                    nuevo_personaje = carpintero(nombre)
                    self.ciudadanos += 1
                elif clase == "constructor":
                    print("¿Qué nombre tendrá el nuevo Constructor?")
                    nombre = input("Nombre: ").strip()
                    nuevo_personaje = constructor(nombre)
                    self.ciudadanos += 1
                elif clase == "bufon":
                    print("¿Qué nombre tendrá el nuevo Bufón?")
                    nombre = input("Nombre: ").strip()
                    nuevo_personaje = bufon(nombre)
                    self.ciudadanos += 1
                elif clase == "profeta":
                    print("¿Qué nombre tendrá el nuevo Profeta?")
                    nombre = input("Nombre: ").strip()
                    nuevo_personaje = profeta(nombre)
                    self.ciudadanos += 1
                else:
                    print("Clase no válida, por favor elige una clase correcta.")
                    return  # Salimos si la clase no es válida

                self.recursos.carne -= 30  # Restamos 30 recursos tras crear el personaje
                print(f"Personaje creado: {nuevo_personaje.nombre}, Clase: {nuevo_personaje.clase}")
                personajesDisponibles.insertRear(nuevo_personaje)

            else:
                print(f"No tienes carne suficiente para generar un nuevo ciudadano. Te faltan {30 - self.recursos.carne} unidades.")

class cuartel:
    def __init__(self):
        self.centro = centro
        self.recursos = recursos

    def crear_personaje_guerrero(self):
        print(self.recursos.casas, self.centro.ciudadanos)
        if  self.centro.ciudadanos >= ((self.recursos.casas) * 4):
            print("No tienes suficientes casas para generar mas personajes")
        else:
            if self.recursos.carne > 30:  # Si tienes recursos suficientes
                print("Selecciona la clase del nuevo personaje: Soldado, Jinete.")
                clase = input("Clase: ").strip().lower()  # Input para clase y pasamos a minúsculas para evitar errores

                if clase == "soldado":
                    print("¿Qué nombre tendrá el nuevo Soldado?")
                    nombre = input("Nombre: ").strip()
                    nuevo_personaje = soldado(nombre)
                    self.centro.ciudadanos += 1
                elif clase == "jinete":
                    print("¿Qué nombre tendrá el nuevo Jinete?")
                    nombre = input("Nombre: ").strip()
                    nuevo_personaje = jinete(nombre)
                    self.centro.ciudadanos += 1
                else:
                    print("Clase no válida, por favor elige una clase correcta.")
                    return  # Salimos si la clase no es válida

                self.recursos.carne -= 30  # Restamos 30 recursos tras crear el personaje
                print(f"Personaje creado: {nuevo_personaje.nombre}, Clase: {nuevo_personaje.clase}")
                personajesDisponibles.insertRear(nuevo_personaje)

            else:
                print(f"No tienes carne suficiente para generar un nuevo ciudadano. Te faltan {30 - self.recursos.carne} unidades.")

class raid:
    def __init__(self):
        self.centro = centro
        self.recursos = recursos
    
    def Raid(self):
        self.centro = centro
        self.recursos = recursos
        
        raid = random.randint(0,100)
        if raid <= 20:
            print("¡Están Atacando tu Aldea!")
            time.sleep(2)
            # Guardamos los valores anteriores para mostrar cuánto se perdió
            recursos_anteriores = {
                'madera': self.recursos.madera,
                'minerales': self.recursos.minerales,
                'piedra': self.recursos.piedra,
                'carne': self.recursos.carne,
                'moneda': self.recursos.moneda,
                'casas': self.recursos.casas,
                'almacenes': self.recursos.almacenes
            }
            
            # Aplicamos pérdidas aleatorias a cada recurso
            self.recursos.madera -= random.randint(10,40)
            self.recursos.minerales -= random.randint(10,40)
            self.recursos.piedra -= random.randint(10,40)
            self.recursos.carne -= random.randint(10,40)
            self.recursos.moneda -= random.randint(10,40)
            
            # Lista para almacenar todas las bajas
            bajas_totales = []
            
            # Probabilidad de perder estructuras (15% de probabilidad para cada estructura)
            if random.randint(0,100) <= 15 and self.recursos.casas > 0:
                casas_perdidas = random.randint(1, min(2, self.recursos.casas))  # Máximo 2 casas perdidas
                self.recursos.casas -= casas_perdidas
                print(f"\n¡Han destruido {casas_perdidas} casa(s)!")
                time.sleep(2)
                
            if random.randint(0,100) <= 15 and self.recursos.almacenes > 0:
                almacenes_perdidos = random.randint(1, min(1, self.recursos.almacenes))  # Máximo 1 almacén perdido
                self.recursos.almacenes -= almacenes_perdidos
                print(f"¡Han destruido {almacenes_perdidos} almacén(es)!")
                time.sleep(2)
                
            # Probabilidad de perder personajes (10% de probabilidad)
            if random.randint(0,100) <= 10 and not personajesDisponibles.isEmpty():
                # Lista temporal para almacenar personajes
                personajes_temp = []
                personajes_perdidos = []
                
                # Sacar todos los personajes a una lista temporal
                while not personajesDisponibles.isEmpty():
                    personajes_temp.append(personajesDisponibles.removeLeft())
                
                # Determinar cuántos personajes se pierden (máximo 2)
                num_perdidos = random.randint(1, min(2, len(personajes_temp)))
                
                # Seleccionar personajes al azar para perder
                for _ in range(num_perdidos):
                    if personajes_temp:  # Si aún hay personajes disponibles
                        indice_perdido = random.randint(0, len(personajes_temp) - 1)
                        personaje_perdido = personajes_temp.pop(indice_perdido)
                        personajes_perdidos.append(personaje_perdido)
                        bajas_totales.append((personaje_perdido.nombre, personaje_perdido.clase))
                        self.centro.ciudadanos -= 1  # Reducir el contador de ciudadanos
                
                # Devolver los personajes sobrevivientes a la cola
                for personaje in personajes_temp:
                    personajesDisponibles.insertRear(personaje)
                    
                # Mostrar mensaje de personajes perdidos
                if personajes_perdidos:
                    print("\nBajas en el ataque:")
                    for personaje in personajes_perdidos:
                        print(f"¡{personaje.nombre} ({personaje.clase}) ha caído en batalla!")
                    time.sleep(2)    
            
            # Nos aseguramos que ningún recurso quede negativo
            self.recursos.madera = max(0, self.recursos.madera)
            self.recursos.minerales = max(0, self.recursos.minerales)
            self.recursos.piedra = max(0, self.recursos.piedra)
            self.recursos.carne = max(0, self.recursos.carne)
            self.recursos.moneda = max(0, self.recursos.moneda)
            
            # Mostramos las pérdidas de recursos
            print("\nPérdidas de Recursos:")
            print(f"Madera: -{recursos_anteriores['madera'] - self.recursos.madera}")
            print(f"Minerales: -{recursos_anteriores['minerales'] - self.recursos.minerales}")
            print(f"Piedra: -{recursos_anteriores['piedra'] - self.recursos.piedra}")
            print(f"Carne: -{recursos_anteriores['carne'] - self.recursos.carne}")
            print(f"Moneda: -{recursos_anteriores['moneda'] - self.recursos.moneda}")
            
            # Mostrar resumen final de estructuras
            print(f"\nResumen final después del ataque:")
            print(f"Estructuras:")
            print(f"- Casas: {self.recursos.casas}")
            print(f"- Almacenes: {self.recursos.almacenes}")
            print(f"Población total: {self.centro.ciudadanos}")
            
            # Mostrar resumen de bajas
            if bajas_totales:
                print("\nPersonajes caídos en batalla:")
                for nombre, clase in bajas_totales:
                    print(f"- {nombre} ({clase})")
            else:
                print("\nNo hubo bajas entre los personajes")
            time.sleep(10)

if __name__ == "__main__":
    acciones = Queue()
    personajesDisponibles = MyDeque()
    personajesOcupados = MyDeque()
    recursos = Recursos()
    centro = centro_de_recoleccion()
    raid_prob = raid()
    personajesDisponibles.insertRear(carpintero("Luis Miguel"))
    personajesDisponibles.insertRear(minero("Oscar"))
    personajesDisponibles.insertRear(soldado("Angel"))
    personajesDisponibles.insertRear(leñador("Manuel"))
    MenuAcciones(acciones)
    RealizarAccion(acciones, personajesDisponibles)
    