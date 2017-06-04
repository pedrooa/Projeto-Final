import pygame as pg
from os import path
game_folder = path.dirname(__file__)
#game settings
vetor = pg.math.Vector2
TRAVE_W = 60
TRAVE_H = 120
TRAVE_H_maior = 170
TRAVE_H_menor = 80
FPS = 2*30

#Configuracoes do jogador
PLAYER_W = 50
PLAYER_H = 50
PLAYER_RAIO = 24
WIDTH = 876
HEIGHT = 573
vel_pulo = -12*2/3
aceleração_maxima = 0.9/2
atrito = -0.12
atrito_powerup = -0.07
atrito_gelo = -0.30
gravidade = 0.7/2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#configuracoes bola
BOLA_W = 22
BOLA_H = 22
arrasto = 0.999
elasticidade = 0.75
gravidade_bola = 0.4/2
atrito_bola = - 0.10/2

#powerups
POWERUP_TIME = 10000
#SCORE
player1_score = 0
player2_score = 0
timer = 0

#carregar musica
pg.mixer.init()
bola_som=pg.mixer.Sound('Musicas/batida_bola.wav')
bola_som.set_volume(1.0)


