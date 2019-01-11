import pygame
import random

pygame.init()
velocidad = [random.randint(1,5),random.randint(1,5)]

screen = pygame.display.set_mode( (800,600) )

#He cargado mi sprite en memoria
spr_ball = pygame.image.load("assets/soccer.png")
spr_ball = pygame.transform.scale(spr_ball, (64,64))
rect_ball = spr_ball.get_rect()


#Game Loop
terminado = False
while not terminado:
    #gestionar los eventos del usuario
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminado = True
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rect_ball = rect_ball.move([10,0])
            elif event.key == pygame.K_LEFT:
                rect_ball = rect_ball.move([-10,0])
            elif event.key == pygame.K_UP:
                rect_ball = rect_ball.move([0,-10])
            elif event.key == pygame.K_DOWN:
                rect_ball = rect_ball.move([0,10])
    #actualizar los estados del juego
    """if velocidad[0] > 0:
        velocidad[0] = random.randint(1,5)
    else:
        velocidad[0] = random.randint(-5,-1)
    if velocidad[1] > 0:
        velocidad[1] = random.randint(1,5)
    else:
        velocidad[1] = random.randint(-5,-1)
    rect_ball = rect_ball.move(velocidad)
    if rect_ball.y > 536:
        velocidad[1] = random.randint(-5,-1)
    if rect_ball.y <= 0:
        velocidad[1] = random.randint(1,5)
    if rect_ball.x > 736:
        velocidad[0] = random.randint(-5,-1)
    if rect_ball.x <= 0:
        velocidad[0] = random.randint(1,5)"""
    #renderizar la interfaz grafica
    screen.fill((0,0,0))
    screen.blit(spr_ball, rect_ball)
    pygame.display.flip()
