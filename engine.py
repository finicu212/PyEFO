#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, sys, math

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

FPS = 144

screen = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('engine')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

delta_t = 0.1

pygame.draw.circle(screen, WHITE, (int(200), int(200)), 3)

sound1 = pygame.mixer.Sound("hi.ogg")
sound2 = pygame.mixer.Sound("low.ogg")

while True:
    inpt = input("press enter")
    sound1.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
