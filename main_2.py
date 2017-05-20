from variaveis import *
import pygame, funcoes, classes, math
from os import path

#Inicia pygame
pygame.init()
pygame.mixer.init()

running = True
while running:
	funcoes.gameLoop()
	funcoes.gameEvents()
	funcoes.gameDraw()
	funcoes.gameScoreTime()
	funcoes.gameQuit()
	
