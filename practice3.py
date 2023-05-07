
# Importar módulos
import pygame
import random

# Inicializar pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Definir dimensiones de la pantalla
ANCHO = 600
ALTO = 600

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Establecer el título de la ventana
pygame.display.set_caption("Snake")

# Crear una lista para almacenar los segmentos de la serpiente
serpiente = []

# Crear una clase para representar los segmentos de la serpiente
class Segmento(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, x, y):
        # Llamar al constructor de la clase padre
        super().__init__()

        # Establecer el ancho y el alto del segmento
        self.image = pygame.Surface([10, 10])
        self.image.fill(VERDE)

        # Establecer la posición del segmento
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # Método para mover el segmento
    def mover(self, dx, dy):
        # Actualizar la posición del segmento
        self.rect.x += dx * 10
        self.rect.y += dy * 10

# Crear un grupo para almacenar los sprites de la serpiente
grupo_serpiente = pygame.sprite.Group()

# Crear el segmento inicial de la serpiente y añadirlo a la lista y al grupo
segmento_inicial = Segmento(300, 300)
serpiente.append(segmento_inicial)
grupo_serpiente.add(segmento_inicial)

# Crear una variable para almacenar la dirección de la serpiente
direccion = "derecha"

# Crear una variable para almacenar el puntaje del jugador
puntaje = 0

# Crear una fuente para renderizar el texto del puntaje
fuente = pygame.font.SysFont("Arial", 32)

# Crear una clase para representar la comida de la serpiente
class Comida(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        # Llamar al constructor de la clase padre
        super().__init__()

        # Establecer el ancho y el alto de la comida
        self.image = pygame.Surface([10, 10])
        self.image.fill(ROJO)

        # Establecer la posición de la comida de forma aleatoria
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, ANCHO - 10, 10)
        self.rect.y = random.randrange(0, ALTO - 10, 10)

    # Método para cambiar la posición de la comida de forma aleatoria
    def cambiar(self):
        self.rect.x = random.randrange(0, ANCHO - 10, 10)
        self.rect.y = random.randrange(0, ALTO - 10, 10)

# Crear un sprite para la comida y añadirlo a un grupo
comida = Comida()
grupo_comida = pygame.sprite.Group()
grupo_comida.add(comida)

# Crear un reloj para controlar el bucle principal
reloj = pygame.time.Clock()

# Crear una variable para controlar el bucle principal
terminado = False

# Bucle principal del juego
while not terminado:
    # Procesar los eventos del teclado y el ratón
    for evento in pygame.event.get():
        # Si el usuario hace clic en cerrar
        if evento.type == pygame.QUIT:
            # Salir del bucle principal
            terminado = True

        # Si el usuario presiona una tecla
        elif evento.type == pygame.KEYDOWN:
            # Si presiona la flecha izquierda y no va hacia la derecha
            if evento.key == pygame.K_LEFT and direccion != "derecha":
                # Cambiar la dirección a izquierda
                direccion = "izquierda"
            # Si presiona la flecha derecha y no va hacia la izquierda
             elif evento.key == pygame.K_RIGHT and direccion != "izquierda":
                direccion = "derecha"




