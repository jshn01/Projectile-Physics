import pygame
from ball import projectile
from settings import pixelsPerMetre as px
from settings import FLOOR, FPS
pygame.init()
import math
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

ball = projectile(0, 0 , 0.2 * px)
angle = 0
initialVel = float(0)

def screenBlitzting(textAngle, textInitialVel, textCoords, textFPS, textToReset):
    screen.blit(textAngle, (10, 660))
    screen.blit(textInitialVel, (10, 685))
    screen.blit(textCoords, (1150, 10))
    screen.blit(textFPS, (10, 10))
    screen.blit(textToReset, (1115, 695))

retry = True
running = True
while running:
    dt = clock.tick(FPS) / 1000
    dt = min(dt, 1/FPS)
    fps = clock.get_fps()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and not ball.placed and event.button == 1:
            ball.pos = pygame.Vector2(pygame.mouse.get_pos())
            ball.placed = True
        if event.type == pygame.MOUSEBUTTONUP and ball.placed and event.button == 3:
             ball.thrown = True
        if event.type == pygame.MOUSEWHEEL:
             if event.y == 1:
                  angle += 1
             if event.y == -1:
                  angle -= 1
        if event.type == pygame.KEYUP:
             if event.key == pygame.K_r:
                  ball.thrown = False
                  ball.placed = False
                  retry = True
                  ball.vel = pygame.Vector2(0,0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if initialVel > 0:
            initialVel -= 1
    if keys[pygame.K_d]:
         initialVel += 1


    textToPlace = font.render("Place Ball using left click, Throw using right click", True, (255,255,255))
    textInitialVel = font.render(f"Initial Velocity: {initialVel}",True, (255,255,255))
    textAngle = font.render(f"Angle: {angle}°", True, (255,255,255))
    textToReset = font.render("Press R to reset", True, (255,255,255))
    screen.fill((0,0,0))
    if not ball.placed:
        screen.blit(textToPlace, (400, 10))
    textFPS = font.render(f"FPS: {int(fps)}", True, (255,255,255))
    textCoords = font.render(f"X: {int(ball.pos.x / px)}, Y: {int(ball.pos.y / px)}", True, (255,255,255))
    screenBlitzting(textAngle=textAngle, textInitialVel=textInitialVel, textCoords=textCoords, textFPS=textFPS, textToReset=textToReset)
    ball.update(dt=dt, screen=screen, floor=FLOOR)
    pygame.display.flip()
    if ball.placed and retry and ball.thrown:
            initialVelY = -initialVel * math.cos(angle * (math.pi / 180))
            initialVelX = initialVel * math.sin(angle * (math.pi / 180))
            ball.vel = pygame.Vector2(initialVelX * px, initialVelY * px)
            retry = False
            clock.tick()

pygame.quit()