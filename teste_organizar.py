# Pygame template - skeleton for a new pygame project
import pygame
import math
from os import path
from settings import *

#funções
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
def playMusicJ3():
    pygame.mixer.music.load("J3.mp3")
    pygame.mixer.music.play(-1, 0.0)
def playMusicNaruto():
    pygame.mixer.music.load("Naruto.mp3")
    pygame.mixer.music.play(-1, 0.0)


# Game loop
running = True
while running:
    #musica
 #   playMusicNaruto()

    if timer2 >= 60:
        break
