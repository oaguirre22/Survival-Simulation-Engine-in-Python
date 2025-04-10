import tkinter as tk
import random
import threading
from queue import Queue

class SupervivenciaSimulacionMovimiento:
    def __init__(self, root, width=800, height=600, num_chars=10, num_resources=20, tile_size=40):
        self.root = root
        self.root.title("Simulacion de Supervivencia - Mapa ASCII")
        
        # Configuración del lienzo con fondo negro
        self.canvas = tk.Canvas(root, width=width, height=height, bg="black")
        self.canvas.pack()
        
        self.width = width
        self.height = height
        self.num_chars = num_chars
        self.num_resources = num_resources
        self.tile_size = tile_size
        self.chars = []
        self.speeds = []
        self.is_moving = False  # Variable de control para el movimiento
        self.action_queue = Queue()  # Cola de acciones
        self.resguardo_position = (width - 100, height - 100)  # Posición del Ayuntamiento
        self.enemies = []  # Lista para almacenar enemigos

        # Emojis y colores para cada tipo de personaje
        self.character_symbols = {
            "Constructor": ("🏗️", "orange"),
            "Cazador": ("🏹", "saddlebrown"),
            "Granjero": ("🌾", "green"),
            "Soldado": ("⚔️", "red"),
            "Pillager": ("🏴‍☠️", "purple"),
        }

        # Colores específicos para cada tipo de recurso
        self.resource_symbols = {
            "Madera": ("🌲", "forestgreen"),
            "Agua": ("💧", "deepskyblue"),
            "Piedra": ("🪨", "darkgray"),
            "Mineral": ("⛏️", "gold"),
            "Moneda": ("💰", "yellow")
        }

        # Inicializar el mapa y personajes
        self.place_resources()
        self.init_characters()
        self.create_ayuntamiento()

        # Iniciar el ciclo día-noche
        self.day = True
        self.change_day_night()

        # Iniciar el hilo para escuchar el comando de terminal
        threading.Thread(target=self.listen_for_move_command, daemon=True).start()

        # Iniciar el ciclo de actualización (movimiento y ejecución de acciones)
        self.update_positions()

    def create_ayuntamiento(self):
        # Dibuja el "Ayuntamiento" para la acción de resguardarse
        x, y = self.resguardo_position
        self.canvas.create_rectangle(x, y, x + 80, y + 80, fill="brown", outline="black")
        self.canvas.create_text(x + 40, y + 40, text="🏛️", font=("Courier", 24), fill="white")
        self.canvas.create_text(x + 40, y + 70, text="Ayuntamiento", font=("Courier", 10), fill="white")

    def place_resources(self):
        # Coloca recursos con colores específicos según el tipo
        for resource, (symbol, color) in self.resource_symbols.items():
            for _ in range(self.num_resources // len(self.resource_symbols)):
                x, y = random.randint(50, self.width - 50), random.randint(50, self.height - 50)
                self.canvas.create_text(x, y, text=symbol, fill=color, font=("Courier", 14))

    def init_characters(self):
        for _ in range(self.num_chars):
            role = random.choice(list(self.character_symbols.keys()))
            char, color = self.character_symbols[role]
            x, y = random.randint(0, self.width), random.randint(0, self.height)
            text = self.canvas.create_text(x, y, text=char, fill=color, font=("Courier", 14))
            self.chars.append({"id": text, "role": role, "x": x, "y": y, "color": color, "target": None, "status_text": None})

    def update_positions(self):
        # Revisa la cola de acciones y asigna una acción si hay una pendiente
        if not self.action_queue.empty():
            action, target_position = self.action_queue.get()
            self.assign_action(action, target_position)

        # Mueve los personajes hacia sus objetivos si tienen un objetivo asignado
        for character in self.chars:
            if character["target"]:
                self.move_character(character)

        # Mueve los enemigos si hay enemigos en el mapa
        self.move_enemies()

        # Llama a la actualización periódicamente
        self.root.after(100, self.update_positions)

    def assign_action(self, action, target_position):
        # Asigna la acción al primer personaje con el rol adecuado
        for character in self.chars:
            if character["role"] == action:
                character["target"] = target_position
                print(f"{character['role']} asignado a realizar la acción en {target_position}")
                
                # Añade un feedback visual al asignar la acción
                if character["status_text"]:
                    self.canvas.delete(character["status_text"])
                character["status_text"] = self.canvas.create_text(character["x"], character["y"] - 10, text=action.capitalize(), fill="white")
                
                break

    def move_character(self, character):
        # Mueve el personaje hacia su objetivo
        char_id = character["id"]
        x, y = self.canvas.coords(char_id)
        target_x, target_y = character["target"]

        # Calcula el movimiento en x y y hacia el objetivo
        dx = 2 if x < target_x else -2 if x > target_x else 0
        dy = 2 if y < target_y else -2 if y > target_y else 0

        # Mueve el personaje en el lienzo
        self.canvas.move(char_id, dx, dy)

        # Verifica si el personaje ha llegado a su destino
        if abs(x - target_x) < 5 and abs(y - target_y) < 5:
            character["target"] = None  # Limpia el objetivo al llegar
            if character["status_text"]:
                self.canvas.delete(character["status_text"])  # Elimina el feedback de estado

            # Añade animación de acción
            self.create_action_animation(x, y, character["role"])

    def create_action_animation(self, x, y, action):
        # Asigna un símbolo según el tipo de acción
        if action == "Granjero":
            symbol = "🌾"
        elif action == "Constructor":
            symbol = "🏗️"
        elif action == "Cazador":
            symbol = "🏹"
        elif action == "Soldado":
            symbol = "⚔️"
        else:
            symbol = "💤"

        # Muestra la animación y limpia automáticamente después de 700 ms
        anim_id = self.canvas.create_text(x, y, text=symbol, fill="white", font=("Courier", 14))
        self.root.after(700, lambda: self.canvas.delete(anim_id))


    def change_day_night(self):
        # Cambia entre día y noche
        self.day = not self.day
        new_bg = "black" if self.day else "midnightblue"
        self.canvas.config(bg=new_bg)
        
        # Cambiar color de texto si es de noche
        for character in self.chars:
            color = "white" if not self.day else character["color"]
            self.canvas.itemconfig(character["id"], fill=color)
        
        self.root.after(30000, self.change_day_night)  # Cambia cada 30 segundos


    def spawn_enemy_wave(self):
        # Genera una oleada de enemigos
        for _ in range(3):  # Genera 3 enemigos
            x, y = random.randint(0, self.width), random.randint(0, self.height)
            enemy = self.canvas.create_text(x, y, text="💀", fill="red", font=("Courier", 14))
            self.enemies.append({"id": enemy, "x": x, "y": y})

    def move_enemies(self):
        # Mueve los enemigos hacia el ayuntamiento
        ayuntamiento_x, ayuntamiento_y = self.resguardo_position
        for enemy in self.enemies:
            x, y = self.canvas.coords(enemy["id"])
            dx = 1 if x < ayuntamiento_x else -1 if x > ayuntamiento_x else 0
            dy = 1 if y < ayuntamiento_y else -1 if y > ayuntamiento_y else 0
            self.canvas.move(enemy["id"], dx, dy)

    def listen_for_move_command(self):
        while True:
            command = input("Ingrese una acción (farmear, construir, cazar, resguardarse, atacar, oleada): ").strip().lower()
            if command == "farmear":
                self.action_queue.put(("Granjero", (random.randint(50, self.width - 50), random.randint(50, self.height - 50))))
                print("Granjero asignado a farmear.")
            elif command == "construir":
                self.action_queue.put(("Constructor", (random.randint(50, self.width - 50), random.randint(50, self.height - 50))))
                print("Constructor asignado a construir.")
            elif command == "cazar":
                self.action_queue.put(("Cazador", (random.randint(50, self.width - 50), random.randint(50, self.height - 50))))
                print("Cazador asignado a cazar.")
            elif command == "resguardarse":
                self.action_queue.put(("Soldado", self.resguardo_position))
                print("Soldado asignado a resguardarse en el ayuntamiento.")
            elif command == "atacar":
                self.action_queue.put(("Pillager", (random.randint(50, self.width - 50), random.randint(50, self.height - 50))))
                print("Pillager asignado a atacar.")
            elif command == "oleada":
                print("Oleada de enemigos generada.")
                self.spawn_enemy_wave()

    def move_enemies(self):
        ayuntamiento_x, ayuntamiento_y = self.resguardo_position
        for enemy in self.enemies[:]:  # Copia de la lista para evitar problemas al eliminar
            x, y = self.canvas.coords(enemy["id"])
            dx = 1 if x < ayuntamiento_x else -1 if x > ayuntamiento_x else 0
            dy = 1 if y < ayuntamiento_y else -1 if y > ayuntamiento_y else 0
            self.canvas.move(enemy["id"], dx, dy)

            # Elimina el enemigo si está cerca del ayuntamiento
            if abs(x - ayuntamiento_x) < 5 and abs(y - ayuntamiento_y) < 5:
                self.canvas.delete(enemy["id"])
                self.enemies.remove(enemy)




# Crear la ventana de la aplicación
root = tk.Tk()
app = SupervivenciaSimulacionMovimiento(root)
root.mainloop()
