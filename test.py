#!/usr/bin/env python3
import pygame

pygame.init()

win = pygame.display.set_mode ((500, 500))
pygame.display.set_caption("first Game")

x = 50
v = 50
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False
pygame.display.update()
print(event)
pygame.quit()
quit()
