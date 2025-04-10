import os
import time

def animacion_pueblo():
    # Definir los frames de la aldea
    frames = [
        """
           🌳   🏠    🌳
            🏡       🏠
        👤               👤
        """,
        """
           🌳     🏠   🌳
            🏠       🏡
        👤               👤
        """,
        """
           🌳   🏠      🌳
            🏡       🏠
        👤               👤
        """,
        """
           🌳     🏠   🌳
            🏠       🏡
        👤               👤
        """
    ]
    # Bucle para mostrar la animación de la aldea
    for _ in range(5):
        for frame in frames:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(frame)
            time.sleep(0.5)

def animacion_aldeano_picando():
    # Definir los frames del aldeano picando
    frames = [
        """
          👤
         /|\\
         / \\
        🪓
        """,
        """
          👤
         /|\\
         / \\
        🪓
        """,
        """
          👤
         /|\\
         / \\
        🪓💥
        """,
        """
          👤
         /|\\
         / \\
        🪓
        """
    ]
    # Bucle para mostrar la animación del aldeano picando
    for _ in range(5):
        for frame in frames:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(frame)
            time.sleep(0.5)
            
def animacion_aldeano_cazando():
    # Definir los frames del aldeano cazando
    frames = [
        """
        👤       🏹           🦌
        """,
        """
        👤       🏹         ➳ 🦌
        """,
        """
        👤       🏹       ➳   🦌
        """,
        """
        👤       🏹     ➳     🦌
        """,
        """
        👤       🏹   ➳       🦌
        """,
        """
        👤       🏹 ➳         🦌
        """,
        """
        👤       🏹           🦌💀
        """,
        """
        👤       🏹           🦌
        """
    ]
    for _ in range(3):  # Repetir la animación de caza
        for frame in frames:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(frame)
            time.sleep(0.3)  # Velocidad de la animación



def animacion_construccion_casa():
    # Definimos los frames de la animación de construcción de la casa
    frames = [
        """
            ⛏️  🧱
        """,
        """
            ⛏️  🧱
            ▄
        """,
        """
            ⛏️  🧱
           ▄██▄
        """,
        """
            ⛏️  🧱
          ▄████▄
        """,
        """
            ⛏️  🧱
         ▄██████▄
        """,
        """
            ⛏️  🧱
        ▄████████▄
        """,
        """
            ⛏️  🧱
        ▄████████▄
        ██████████
        """,
        """
            ⛏️  🧱
        ▄████████▄
        ██████████
        ██████████
        """,
        """
            ⛏️  🧱
        ▄████████▄
        ██████████
        ██████████
        🏠 ¡Casa terminada!
        """
    ]
    for _ in range(3):  # Número de veces que se repetirá la animación completa
        for frame in frames:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(frame)
            time.sleep(0.5)  # Pausa entre frames para simular el proceso de construcción
            

def animacion_ataque_aldea():
    # Definir los frames para la animación del ataque a la aldea
    frames = [
        """
           🌳   🏠    🌳
            🏡       🏠
        👤               👤
        
        ➹
        """,
        """
           🌳   🏠    🌳
            🏡       🏠
        👤               👤
        
          ➹
        """,
        """
           🌳   🏠    🌳
            🏡       🏠
        👤               👤
        
            ➹
        """,
        """
           🌳   🏠    🌳
            🏡       🏠
        👤               👤
        
              💥
        """,
        """
           🌳   🏚️    🌳
            🏚️       🏚️
        👤               👤
        """
    ]
    
    # Mostrar cada frame por 0.5 segundos
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(0.5)
        