import pygame as pg

#game settings
vetor = pg.math.Vector2
TRAVE_W = 60
TRAVE_H = 120
TRAVE_H_maior = 200
TRAVE_H_menor = 80


BOLA_W = 34
BOLA_H = 34
PLAYER_W = 50
PLAYER_H = 50
PLAYER_RAIO = 24
WIDTH = 876
HEIGHT = 573
FPS = 40
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#setting para a movimentacao com vetor
aceleração_maxima = 0.9
atrito = -0.12
gravidade = 0.7

#configuracoes bola
arrasto = 0.999
elasticidade = 0.75
gravidade_bola = 0.2
atrito_bola = - 0.10

#powerups
POWERUP_TIME = 10000
#SCORE
player1_score = 0
player2_score = 0
timer = 0

#Musicas
Naruto = "Naruto.mp3"
J3 = "J3.mp3"
