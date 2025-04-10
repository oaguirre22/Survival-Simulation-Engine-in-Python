
from tkinter import*
from PIL import Image, ImageTk
import pygame
from Clases import*
from tkinter import messagebox  # Importar messagebox para mostrar advertencias
import time
import random

pygame.mixer.init()
acciones = Queue()
ColaPrioridad = PQueueAP()
     
def AccionesJuego(opcion):
        if opcion == "Farmear":
            messagebox.showinfo(message = "Farmear se ha agregado a la cola de tareas")
            acciones.enqueue("Farmear")
        elif opcion == "Construir":
            messagebox.showinfo(message= "Construir se ha agregado a la cola de tareas")
            acciones.enqueue("Construir")
        elif opcion == "Cazar":
            messagebox.showinfo(message= "Cazar se ha agregado a la cola de tareas")
            acciones.enqueue("Cazar")
        elif opcion == "Resguardarse":
            messagebox.showinfo(message= "Resguardarse se ha agregado a la cola de tareas")
            acciones.enqueue("Resguardarse")
        elif opcion == "Atacar":
            messagebox.showinfo(message = "Atacar se ha agregado a la cola de tareas")
            acciones.enqueue("Atacar")
        elif opcion == "Realizar Tareas": 
            RealizarAcciones(acciones, personajesDisponibles)
            
        else:
            messagebox.showinfo(message= "Opción no válida")
        
        if acciones.size() > 4:
            messagebox.showinfo(message= "La aldea esta realizando las tareas")
            RealizarAcciones(acciones, personajesDisponibles)

def RealizarAcciones(acciones, PersonajesDisponibles):
    if acciones.empty():
        messagebox.showwarning( message = "No hay acciones en espera")
        return 
    
    while not acciones.empty():
        accion = acciones.dequeue()
        mejorPersonaje = None
        mejorCompatibilidad = -1
        
        for personaje in PersonajesDisponibles:
            compat = Compatibilidad(personaje, accion)
            
            if compat is None:
                continue
            if compat >= mejorCompatibilidad:
                mejorPersonaje = personaje
                mejorCompatibilidad = compat
                
        if mejorPersonaje:
            if accion == "Atacar":
                prioridad = 1
            elif accion == "Resguardarse":
                prioridad = 2
            elif accion == "Farmear":
                prioridad = 3
            elif accion == "Construir":
                prioridad = 4
            elif accion == "Cazar":
                prioridad = 5
            
            ColaPrioridad.enqueue((prioridad, accion, mejorPersonaje))
            personajesDisponibles.remove(mejorPersonaje)
    
    PrioridadAldea()
    raid_prob()

def PrioridadAldea():

    while not ColaPrioridad.empty():
        prioridad, accion, personaje = ColaPrioridad.dequeue()
        

        if accion == "Farmear":
            textJuego.insert(END, f"{personaje.nombre} esta: FARMEANDO [🌾...🌿...🌿...🌾]\n")
            
        elif accion == "Construir":
                textJuego.insert(END, "Que tipo de recurso quieres farmear?\n")
                textJuego.insert(END, "1.- Casa\n")
                textJuego.insert(END, "2.- Almacem\n")
                EntryConstruccion = Entry(rootAldea)
                EntryConstruccion.place(x=300, y=160)
                btn_confirmar = Button(rootAldea, text="Confirmar", command=lambda: r())
                btn_confirmar.place(x=450, y=160)

                def r():
                    c_op = EntryConstruccion.get()
                    EntryConstruccion.destroy()
                    btn_confirmar.destroy()
                    
                    if c_op == "1":
                        textJuego.insert(END, "Haz seleccionado construir casa \n")
                        recursos.construccion_casa()
                    elif c_op == "2":
                        textJuego.insert(END, "Haz seleccionado construir piedra \n")
                        recursos.construccion_almacen()
                                 
        elif accion == "Cazar":
                textJuego.insert(END, f"{personaje.nombre} esta: CAZANDO [🏹...🦌...🏹] Caza completada.\n")
        elif accion == "Resguardarse":
                textJuego.insert(END, f"{personaje.nombre}esta: RESGUARDANDOSE [🔒...🏠...🔒] Resguardo completado.\n")
        elif accion == "Atacar":
                textJuego.insert(END, f"{personaje.nombre} esta: ATACANDO [⚔️...💥...⚔️] Ataque completado.\n")
                
        recursos.recolectar(personaje, accion)
        personajesOcupados.insertRear(personaje)
        textJuego.see(END)
        rootAldea.update()  
        time.sleep(8)  
        
            
def Compatibilidad( personaje, accion):
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
        self.carne = 0
        self.moneda = 100
        self.casas = 2
        self.almacenes = 1
        self.ciudadanos = 4

    def recolectar(self, personaje, accion):
        global btn_confirmar
        compat = Compatibilidad(personaje, accion)
        compat = compat if compat is not  None else 1.0
        cantidad = int(random.randint(30, 50) * compat)  # Generar recursos basado en compatibilidad
        cantidad2 = int(random.randint(5, 20) * compat)
        
        if compat:
            if accion == "Farmear":
                textJuego.insert(END, "Que tipo de recurso quieres farmear?\n")
                textJuego.insert(END, "1.- Madera\n")
                textJuego.insert(END, "2.- Piedra\n")
                
                entry_recurso = Entry(rootAldea)
                entry_recurso.place(x=300, y=160)
                btn_confirmar = Button(rootAldea, text="Confirmar", command=lambda: r())
                btn_confirmar.place(x=450, y=160)
                
                def r():
                    recurso_op = entry_recurso.get()
                    entry_recurso.destroy()
                    btn_confirmar.destroy()
                    
                    if recurso_op == "1":
                        textJuego.insert(END, "Haz seleccionado recolectar madera.\n")
                        
                        if isinstance(personaje, leñador):
                            new_cantidad = cantidad*2
                            self.madera += new_cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {new_cantidad} de madera.\n")
                        elif isinstance(personaje, minero):
                            self.madera += cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de madera.\n")
                        elif isinstance(personaje, soldado):
                            self.madera += cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de madera.\n")
                        elif isinstance(personaje, jinete):
                            self.madera += cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de madera.\n")
                        elif isinstance(personaje, carpintero):
                            self.madera += cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de madera.\n")
                        elif isinstance(personaje, constructor):
                            self.madera += cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de madera.\n")
                        elif isinstance(personaje, bufon):
                            self.madera += cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de madera.\n")
                        elif isinstance(personaje, profeta):
                            self.madera += cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de madera.\n")
                            
                    elif recurso_op == "2":
                        textJuego.insert(END, "Haz seleccionado recolectar piedra.\n")
                        if isinstance(personaje, minero):
                            new_cantidad = cantidad*2
                            self.piedra += new_cantidad
                            self.minerales += cantidad2
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {new_cantidad} de piedra y {cantidad2} minerales.\n")
                        elif isinstance(personaje, leñador):
                            self.piedra += cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de piedra.\n")
                        elif isinstance(personaje, soldado):
                            self.piedra += cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de piedra.\n")
                        elif isinstance(personaje, jinete):
                            self.piedra += cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de piedra.\n")
                        elif isinstance(personaje, carpintero):
                            self.piedra += cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de piedra.\n")
                        elif isinstance(personaje, constructor):
                            self.piedra += cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de piedra.\n")
                        elif isinstance(personaje, bufon):
                            self.piedra += cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de piedra.\n")
                        elif isinstance(personaje, profeta):
                            self.piedra += cantidad
                            textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de piedra.\n")
                            
            if accion == "Cazar":
                if isinstance(personaje, soldado):
                    self.carne += cantidad
                    textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de carne.\n")
                    print(self.carne)
                elif isinstance(personaje, jinete):
                    self.carne += cantidad
                    textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} carne.\n")
                elif isinstance(personaje, leñador):
                    self.carne += cantidad2
                    textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de carne.\n")
                elif isinstance(personaje, minero):
                    self.madera += cantidad
                    self.piedra += cantidad
                    textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de carne.\n")
                elif isinstance(personaje, carpintero):
                    self.madera += cantidad
                    textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de carne.\n")
                elif isinstance(personaje, constructor):
                    self.piedra += cantidad
                    textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de carne.\n")
                elif isinstance(personaje, bufon):
                    self.moneda += cantidad
                    textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de carne.\n")
                elif isinstance(personaje, carpintero):
                    self.moneda += cantidad
                    textJuego.insert(END, f"{personaje.nombre} ha recolectado {cantidad} de carne.\n")
                    
            textJuego.see(END)
            rootAldea.update()  # Actualizar la ventana para ver el progreso
            time.sleep(3)

    def construccion_casa(self):
        if self.madera < 50:
            textJuego.insert(END, f"No tienes la madera suficiente para construir una casa. Te faltan {50 - self.madera} unidades.\n")
        elif self.piedra < 50:
            textJuego.insert(END, f"No tienes la piedra suficiente para construir una casa.Te faltan {50 - self.piedra} unidades.\n")
        elif self.moneda < 25:
            textJuego.insert(END, f"No tienes las monedas suficientes para construir una casa.Te faltan {25 - self.moneda} unidades.\n")
        else:
            textJuego.insert(END, "Construyendo casa...\n")
            self.madera -= 50
            self.piedra -= 50
            self.moneda -= 25
            self.casas += 1
            
            textJuego.insert(END, f"Casa construida. Total casas: {self.casas}\n")
        
        textJuego.see(END)
        rootAldea.update()  # Actualizar la ventana para ver el progreso
        time.sleep(2)
        
    def construccion_almacen(self):
        if self.madera < 70:
            textJuego.insert(END, f"No tienes la madera suficiente para construir un almacen.Te faltan {70 - self.madera} unidades.\n")
        elif self.piedra < 70:
            textJuego.insert(END, f"No tienes la piedra suficiente para construir un almacen. Te faltan {70 - self.piedra} unidades.\n")
        elif self.moneda < 35:
            textJuego.insert(END, f"No tienes las monedas suficientes para construir un almacen. Te faltan {35 - self.moneda} unidades.\n")
        else:
            textJuego.insert(END, "Construyendo almacen...\n")
            self.madera -= 70
            self.piedra -= 70
            self.moneda -= 35
            self.almacenes += 1
            
        textJuego.see(END)
        rootAldea.update()  # Actualizar la ventana para ver el progreso
        time.sleep(2)
    
    def crear_personaje_recolector(self):
        global btn_confirmar1
        nombres_aleatorios = ["Miguel", "Luis", "Carlos", "Ana", "Laura", "Sofía", "Juan", "Diana"]
        print(self.casas)
        if self.ciudadanos >= ((self.casas) * 4):
            textRecolector.insert(END, "No tienes suficientes casas para generar mas personajes\n")
        else:
            print(self.carne)
            if self.carne >= 30:  # Si tienes recursos suficientes
                textRecolector.insert(END, "Selecciona la clase del nuevo personaje: Leñador, Minero, Carpintero, Constructor, Bufon o Profeta.\n")
                
                # Crear entrada para la clase
                entry_clase1 = Entry(rootRecolector)
                entry_clase1.place(x=225, y=80)
                btn_confirmar1 = Button(rootRecolector, text="Confirmar Clase", command= lambda: confirmar_clase())
                btn_confirmar1.place(x=235, y=100)
                
                def confirmar_clase():
                    c = entry_clase1.get()
                    entry_clase1.destroy()
                    btn_confirmar1.destroy()
                    
                    if c == "leñador":
                        textRecolector.insert(END, "¿Qué nombre tendrá el nuevo Leñador?")
                        n = random.choice(nombres_aleatorios)
                        nuevo_personaje = leñador(n)
                        self.ciudadanos += 1
                    elif c == "minero":
                        textRecolector.insert(END, "¿Qué nombre tendrá el nuevo Minero?")
                        n = random.choice(nombres_aleatorios)
                        nuevo_personaje = minero(n)
                        self.ciudadanos += 1
                    elif c == "carpintero":
                        textRecolector.insert(END,"¿Qué nombre tendrá el nuevo Carpintero?")
                        n = random.choice(nombres_aleatorios)
                        nuevo_personaje = carpintero(n)
                        self.ciudadanos += 1
                    elif c == "constructor":
                        textRecolector.insert(END,"¿Qué nombre tendrá el nuevo Constructor?")
                        n = random.choice(nombres_aleatorios)
                        nuevo_personaje = constructor(n)
                        self.ciudadanos += 1
                    elif c == "bufon":
                        textRecolector.insert(END,"¿Qué nombre tendrá el nuevo Bufón?")
                        n = random.choice(nombres_aleatorios)
                        nuevo_personaje = bufon(n)
                        self.ciudadanos += 1
                    elif c == "profeta":
                        textRecolector.insert(END,"¿Qué nombre tendrá el nuevo Profeta?")
                        n = random.choice(nombres_aleatorios)
                        nuevo_personaje = profeta(n)
                        self.ciudadanos += 1
                    else:
                        textRecolector.insert(END,"Clase no válida, por favor elige una clase correcta.")
                        return
                    self.carne -= 30
                    textRecolector.insert(END, f"Personaje creado: {nuevo_personaje.nombre}, Clase: {nuevo_personaje.clase}\n")
                    personajesDisponibles.insertRear(nuevo_personaje)
                    for valor in personajesDisponibles:
                        print(valor)
                    
                    
            else:
                textRecolector.insert(END, f"No tienes carne suficiente para generar un nuevo ciudadano. Te faltan {30 - self.carne} unidades.\n")
        
        textRecolector.see(END)
        rootRecolector.update()
        
    def CrearGuerrero(self):
        global btn_confirmar, entry_nombre, entry_clase
        print(self.casas, self.ciudadanos)
        if self.ciudadanos >= ((self.casas) * 4):
            textCuartel.insert(END, "No tienes suficientes casas para generar mas personajes\n")
        else:
            print(self.carne)
            if self.carne >= 30:  # Si tienes recursos suficientes
                textCuartel.insert(END, "Selecciona la clase del nuevo personaje: Soldado, Jinete.\n")
                
                # Crear entrada para la clase
                entry_clase = Entry(rootCuartel)
                entry_clase.place(x=410, y = 40)
                btn_confirmar = Button(rootCuartel, text="Confirmar Clase", command= lambda: confirmar_clase())
                btn_confirmar.place(x=420, y=70)
                
                
                def confirmar_clase():
                    clase = entry_clase.get()
                    entry_clase.destroy()
                    btn_confirmar.destroy()
                    
                    if clase in ["soldado", "jinete"]:
                        textCuartel.insert(END, f"¿Qué nombre tendrá el nuevo {clase.title()}?\n")
                        
                        # Crear entrada para el nombre
                        entry_nombre = Entry(rootCuartel)
                        entry_nombre.place(x=410, y = 40)
                        
                        def confirmar_nombre():
                            nombre = entry_nombre.get().strip()
                            entry_nombre.destroy()
                            btn_confirmar_nombre.destroy()
                            
                            if clase == "soldado":
                                nuevo_personaje = soldado(nombre)
                            elif clase == "jinete":
                                nuevo_personaje = jinete(nombre)
                                
                            self.ciudadanos += 1
                            self.carne -= 30
                            textCuartel.insert(END, f"Personaje creado: {nuevo_personaje.nombre}, Clase: {nuevo_personaje.clase}\n")
                            personajesDisponibles.insertRear(nuevo_personaje)
                            
                        btn_confirmar_nombre = Button(rootCuartel, text="Confirmar Nombre", command= lambda:confirmar_nombre())
                        btn_confirmar_nombre.place(x = 420, y = 70)
                        
                    else:
                        textCuartel.insert(END, "Clase no válida, por favor elige una clase correcta.\n")
                
                
            else:
                textCuartel.insert(END, f"No tienes carne suficiente para generar un nuevo ciudadano. Te faltan {30 - self.carne} unidades.\n")
        
        textCuartel.see(END)
        rootCuartel.update()
        
        




class raid:
    def __init__(self):
        
        self.recursos = recursos
    
    def Raid(self):
        raid = random.randint(0,100)
        if raid <= 20:
            messagebox.showwarning(message ="¡Están Atacando tu Aldea!")
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
                messagebox.showwarning(message =f"¡Han destruido {casas_perdidas} casa(s)!")
                time.sleep(2)
                
            if random.randint(0,100) <= 15 and self.recursos.almacenes > 0:
                almacenes_perdidos = random.randint(1, min(1, self.recursos.almacenes))  # Máximo 1 almacén perdido
                self.recursos.almacenes -= almacenes_perdidos
                messagebox.showwarning(message = f"¡Han destruido {almacenes_perdidos} almacén(es)!")
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
                        self.ciudadanos -= 1  # Reducir el contador de ciudadanos
                
                # Devolver los personajes sobrevivientes a la cola
                for personaje in personajes_temp:
                    personajesDisponibles.insertRear(personaje)
                    
                # Mostrar mensaje de personajes perdidos
                if personajes_perdidos:
                    for personaje in personajes_perdidos:
                        messagebox.showwarning(message =f"¡{personaje.nombre} ({personaje.clase}) ha caído en batalla!")
                    time.sleep(2)    
            
            # Nos aseguramos que ningún recurso quede negativo
            self.recursos.madera = max(0, self.recursos.madera)
            self.recursos.minerales = max(0, self.recursos.minerales)
            self.recursos.piedra = max(0, self.recursos.piedra)
            self.recursos.carne = max(0, self.recursos.carne)
            self.recursos.moneda = max(0, self.recursos.moneda)
            
            # Mostramos las pérdidas de recursos
            textRaid.insert(END, "\nPérdidas de Recursos:")
            textRaid.insert(END, f"Madera: -{recursos_anteriores['madera'] - self.recursos.madera}")
            textRaid.insert(END, f"Minerales: -{recursos_anteriores['minerales'] - self.recursos.minerales}")
            textRaid.insert(END, f"Piedra: -{recursos_anteriores['piedra'] - self.recursos.piedra}")
            textRaid.insert(END, f"Carne: -{recursos_anteriores['carne'] - self.recursos.carne}")
            textRaid.insert(END, f"Moneda: -{recursos_anteriores['moneda'] - self.recursos.moneda}")
            
            # Mostrar resumen final de estructuras
            textRaid.insert(END, f"\nResumen final después del ataque:")
            textRaid.insert(END, f"Estructuras:")
            textRaid.insert(END, f"- Casas: {self.recursos.casas}")
            textRaid.insert(END, f"- Almacenes: {self.recursos.almacenes}")
            textRaid.insert(END, f"Población total: {self.ciudadanos}")
            
            # Mostrar resumen de bajas
            if bajas_totales:
                textRaid.insert(END, "\nPersonajes caídos en batalla:")
                for nombre, clase in bajas_totales:
                    textJuego.insert(END, f"- {nombre} ({clase})")
            else:
                textRaid.insert(END, "\n No hubo bajas entre los personajes")
            time.sleep(10)
            
        textRaid.see(END)
        rootJuego.update()
        

    
if __name__ == "__main__":
    acciones = Queue()
    personajesDisponibles = MyDeque()
    personajesOcupados = MyDeque()
    recursos = Recursos()
   # cuartel_g =cuartel(recursos, centro)
    raid_prob = raid()
    personajesDisponibles.insertRear(carpintero("Luis Miguel"))
    personajesDisponibles.insertRear(constructor("Marcelo"))
    personajesDisponibles.insertRear(minero("Oscar"))
    personajesDisponibles.insertRear(soldado("Angel"))
    personajesDisponibles.insertRear(leñador("Manuel"))
    for valor in personajesDisponibles:
        print(valor.nombre, valor.clase)
  
        
            
            


def DarkFantasyAudio():
    pygame.mixer.music.load("C:/Users/angel/OneDrive/Documentos/Universidad (códigos)/Proyecto/Proyecto-Estructuras/DarkFantasy2.mp3") 
    pygame.mixer.music.play(loops=-1)   

     
class GUIjuego:
    def __init__(self, root):
        self.root = root
    
   
    
    def IniciarJuego(self):
        global textRaid, rootJuego
        ################################### CREACION DE LA PAGINA  ############################################################################

        rootJuego = Toplevel(self.root)
        rootJuego.title("THIS IS NOT MINECRAFT")
        rootJuego.geometry("800x600")
        rootJuego.resizable(0,0)
        
        
        
        Imagen2 = Image.open("C:/Users/angel/OneDrive/Documentos/Universidad (códigos)/Proyecto/Proyecto-Estructuras/PantallaPrincipal.png")
        ancho = 600
        alto = 600
        ImagenNueva = Imagen2.resize((ancho, alto))
        ImagenSalida = ImageTk.PhotoImage(ImagenNueva)
        picture = Label(rootJuego, image = ImagenSalida)
        picture.place(x = 200, y = 0)
        
        
        Imagen3 = Image.open("C:/Users/angel/OneDrive/Documentos/Universidad (códigos)/Proyecto/Proyecto-Estructuras/PantallaInicio2.png")
        ancho =200
        alto = 600
        ImagenNueva2 = Imagen3.resize((ancho, alto))
        ImagenSalida2 = ImageTk.PhotoImage(ImagenNueva2)
        picture = Label(rootJuego, image = ImagenSalida2)
        picture.place(x = 0, y = 0)
    
        ################################### BOTONES DE MENU, EDIFICIOS y minerales de la aldea,  ############################################################################
        
        btnMenu = Button(rootJuego, text = "Tareas de la aldea", font = ("forte 12"), bg = "gold", bd = 5, command = self.MenuAldea)
        btnMenu.place(x = 25, y = 100)
        
        btnCreacionPersonaje = Button(rootJuego, text = "Cuartel General", font = ("forte 12"), bg = "gold", bd = 5, command= self.MenuCuartel)
        btnCreacionPersonaje.place(x = 35, y = 200)

        btnCreacionPersonaje = Button(rootJuego, text = "Centro de Recoleccion", font = ("forte 12"), bg = "gold", bd = 5, command= self.MenuRecolector)
        btnCreacionPersonaje.place(x = 20, y = 300)
        
        textRaid = Text(rootJuego, wrap=WORD, width = 20, height=10, font=("forte", 13))
        textRaid.place(x=10, y=400)
        
       
        rootJuego.mainloop()
        
    def MenuAldea(self):
        global textJuego, lista_acciones, rootAldea

        rootAldea = Toplevel(self.root)
        rootAldea.title("Tareas de la aldea")
        rootAldea.resizable(0,0)
        rootAldea.geometry("550x400")  
        Imagen4 = Image.open("C:/Users/angel/OneDrive/Documentos/Universidad (códigos)/Proyecto/Proyecto-Estructuras/Menu.png")
        ancho =550
        alto = 600
        ImagenNueva3 = Imagen4.resize((ancho, alto))
        ImagenSalida3 = ImageTk.PhotoImage(ImagenNueva3)
        picture = Label(rootAldea, image = ImagenSalida3)
        picture.place(x = 0, y = 0)
       
       

        
        
        btn1 = Button(rootAldea, text = "Farmear", font = ("forte 15"), bd = 2 ,command = lambda: AccionesJuego("Farmear")) 
        btn1.place(x = 1, y = 60 ) 
        
        btn2 = Button(rootAldea, text = "Construir", font = ("forte 15"),  bd = 2 ,command = lambda: AccionesJuego("Construir") )
        btn2.place(x = 100, y = 60)
        
        btn3 = Button(rootAldea, text = "Cazar", font = ("forte 15"),  bd = 2 ,command = lambda: AccionesJuego("Cazar") )
        btn3.place(x = 210, y = 60)
        
        btn4 = Button(rootAldea, text = "Resguardarse", font = ("forte 15"),  bd = 2 ,command = lambda: AccionesJuego("Resguardarse"))
        btn4.place(x = 290, y = 60)
        
        btn5 = Button(rootAldea, text = "Atacar", font = ("forte 15"),bd = 2, command = lambda: AccionesJuego("Atacar"))
        btn5.place(x = 450, y = 60)
        
        btn6 = Button(rootAldea, text = "Realizar tarea", font = ("forte 15"),bd = 2,  command = lambda: AccionesJuego("Realizar Tareas") )
        btn6.place(x = 200, y = 110)
        
                
        
        textJuego = Text(rootAldea, wrap=WORD, width=50, height=10, font=("forte", 13))
        textJuego.place(x=40, y=200)
        
        rootAldea.mainloop()
    
    def MenuCuartel(self):
        global textCuartel, lista_acciones, rootCuartel

        rootCuartel = Toplevel(self.root)
        rootCuartel.title("Cuartel")
        rootCuartel.resizable(0,0)
        rootCuartel.geometry("550x400")
        
        Imagen5 = Image.open("C:/Users/angel/OneDrive/Documentos/Universidad (códigos)/Proyecto/Proyecto-Estructuras/PantallaCreacion.png")
        ancho =550
        alto = 400
        ImagenNueva4 = Imagen5.resize((ancho, alto))
        ImagenSalida4 = ImageTk.PhotoImage(ImagenNueva4)
        picture = Label(rootCuartel, image = ImagenSalida4)
        picture.place(x = 0, y = 0)
         
        

        
        
        btn1 = Button(rootCuartel, text = "Crear nuevo personaje Guerrero", font = ("forte 15"), bd = 10, command = lambda: recursos.CrearGuerrero() ) 
        btn1.place(x = 100, y = 300 ) 
                 
        textCuartel = Text(rootCuartel, wrap=WORD, width=20, height=10, font=("forte", 13), bd = 2)
        textCuartel.place(x=170, y=40)
        rootCuartel.mainloop()

    def MenuRecolector(self):
        global textRecolector, lista_acciones, rootRecolector

        rootRecolector = Toplevel(self.root)
        rootRecolector.title("Centro de Recoleccion")
        rootRecolector.resizable(0,0)
        rootRecolector.geometry("550x400")  
        Imagen6 = Image.open("C:/Users/angel/OneDrive/Documentos/Universidad (códigos)/Proyecto/Proyecto-Estructuras/PantallaRecolector.png")
        ancho =550
        alto = 400
        ImagenNueva5 = Imagen6.resize((ancho, alto))
        ImagenSalida5 = ImageTk.PhotoImage(ImagenNueva5)
        picture = Label(rootRecolector, image = ImagenSalida5)
        picture.place(x = 0, y = 0)
         
        

        
        
        btn1 = Button(rootRecolector, text = "Crear nuevo personaje Recolector", font = ("forte 15"), bd = 5, command = lambda: recursos.crear_personaje_recolector() ) 
        btn1.place(x = 140, y = 20 ) 
                 
        textRecolector = Text(rootRecolector, wrap=WORD, width=50, height=10, font=("forte", 13))
        textRecolector.place(x=55, y=180)
        
        rootRecolector.mainloop()
    
##################################################################################################################################################################################

root = Tk()

root.title("Estructura de datos II")
root.geometry("600x500")
root.resizable(0,0)
Imagen = Image.open(
    
    "C:/Users/angel/OneDrive/Documentos/Universidad (códigos)/Proyecto/Proyecto-Estructuras/PantallaInicio.png"
)
ancho = 600
alto = 500
ImagenNueva = Imagen.resize((ancho, alto))
ImagenSalida = ImageTk.PhotoImage(ImagenNueva)
picture = Label(root, image = ImagenSalida)
picture.place(x = 1, y = 0)
app = GUIjuego(root)



btn = Button(root, text = "Iniciar juego", font = ("forte 12"), bg = "brown", bd = 5, command = app.IniciarJuego)
btn.place(x = 250, y = 150)

DarkFantasyAudio()
root.mainloop()
