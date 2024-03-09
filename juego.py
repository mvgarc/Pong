import pygame
from random import randint
import sys

pygame.init()

ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Ejemplo 4")

# Intenta cargar la imagen de la pelota
try:
    ball = pygame.image.load("ball.png")
except pygame.error as e:
    print("Error cargando ball.png:", e)
    pygame.quit()
    sys.exit()

ballrect = ball.get_rect()

# La velocidad se calcula con un valor pseudialeatorio entre 3 y 6
speed = [randint(3,6),randint(3,6)]
ballrect.move_ip(0,0)

# Intenta cargar la imagen del bate
try:
    bate = pygame.image.load("bate.png")
except pygame.error as e:
    print("Error cargando bate.png:", e)
    pygame.quit()
    sys.exit()

baterect = bate.get_rect()
baterect.move_ip(240,450)


