import pygame, math, classes, funcoes
from os import path

#Variaveis gerais
font_name = pygame.font.match_font('arial')
vetor = pygame.math.Vector2
running = True
WIDTH = 876
HEIGHT = 573
FPS = 45

#Cores em Hexadecimal
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Setando para a movimentacao com vetor
aceleração_maxima = 0.9
atrito = -0.12
gravidade = 0.7


#Variaveis Bola
arrasto = 0.999
elasticidade = 0.75
gravidade_bola = 0.2
atrito_bola = - 0.10

#Cria a tela, determina a fonte e inicia o Clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Head Soccer pre-pre-pre-Alpha")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 16)

#carregando Imagens
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, "Imagens")
background = pygame.image.load(path.join(img_folder, 'background2.jpeg')).convert()
background_rect = background.get_rect()
player1_img = pygame.image.load(path.join(img_folder, "cabeca1.png")).convert()
player2_img = pygame.image.load(path.join(img_folder, "cabeca2.png")).convert()
SoccerBall = pygame.image.load(path.join(img_folder, "SoccerBall.png")).convert()
trave_1 = pygame.image.load(path.join(img_folder, "trave_1.png")).convert()
trave_2 = pygame.image.load(path.join(img_folder, "trave_2.png")).convert()

#Sprite Group
all_sprites = pygame.sprite.Group()
plataformas = pygame.sprite.Group()
player2_group = pygame.sprite.Group()
player1_group = pygame.sprite.Group()
todos_jogadores = pygame.sprite.Group()
trave_1_group = pygame.sprite.Group()
trave_2_group = pygame.sprite.Group()

#Criando Objetos
bola = classes.Bola(5,HEIGHT/2,20)
player1 = classes.Jogador(WIDTH*1/3,player1_img,0)
player2 = classes.Jogador(WIDTH*2/3,player2_img,1)
trave1 = classes.Trave_1()
trave2 = classes.Trave_2()
campo_futebol = classes.Campo(0,HEIGHT - 30,WIDTH,30)

#ADD Sprites
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(bola)
all_sprites.add(campo_futebol)
all_sprites.add(trave1)
all_sprites.add(trave2)
plataformas.add(campo_futebol)
player2_group.add(player2)
player1_group.add(player1)
trave_1_group.add(trave1)
trave_2_group.add(trave2)
todos_jogadores.add(player1)
todos_jogadores.add(player2)
