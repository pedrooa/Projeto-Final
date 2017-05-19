import pygame, funcoes, classes, math
from variaveis import *
from os import path

#Inicia pygame
pygame.init()
pygame.mixer.init()

running = True
while running:
	gameLoop()
	gameEvents()
	gameDraw()
	gameQuit()
	
