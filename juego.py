import pygame
from random import randint
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana del juego
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pong")

# Intenta cargar la imagen de la pelota
try:
    ball = pygame.image.load("ball.png")
except pygame.error as e:
    print("Error cargando ball.png:", e)
    pygame.quit()
    sys.exit()

# Obtiene el rectángulo de la pelota
ballrect = ball.get_rect()

# La velocidad de la pelota se calcula con valores pseudialeatorios entre 3 y 6
speed = [randint(3, 6), randint(3, 6)]
ballrect.move_ip(0, 0)

# Intenta cargar la imagen del bate
try:
    bate = pygame.image.load("bate.png")  # Reemplaza "ruta/del/archivo/" con la ruta correcta
except pygame.error as e:
    print("Error cargando bate.png:", e)
    pygame.quit()
    sys.exit()


# Obtiene el rectángulo del bate
baterect = bate.get_rect()
baterect.move_ip(240, 450)

# Configuración de la fuente para el texto en pantalla (tamaño 36)
fuente = pygame.font.Font(None, 36)

# Bucle principal del juego
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Control del movimiento del bate mediante las teclas de flecha izquierda y derecha
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-3, 0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(3, 0)

    # Verifica si el bate colisiona con la pelota y ajusta la dirección de la pelota
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]

    # Mueve la pelota según la velocidad actual
    ballrect = ballrect.move(speed)

    # Verifica colisiones con los bordes de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]

    if ballrect.top < 0:
        speed[1] = -speed[1]

    # Si la pelota toca el borde inferior, muestra "Game Over"
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (125, 125, 125))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
    else:
        # Dibuja el fondo y las imágenes (pelota y bate)
        ventana.fill((252, 243, 207))
        ventana.blit(ball, ballrect)
        ventana.blit(bate, baterect)

    # Actualiza la pantalla
    pygame.display.flip()

    # Controla la velocidad del bucle
    pygame.time.Clock().tick(60)

# Cierra Pygame al salir del bucle principal
pygame.quit()
