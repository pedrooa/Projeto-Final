import pygame

#game settings
vetor = pygame.math.Vector2
TRAVE_W = 60
TRAVE_H = 120
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

#SCORE
player1_score = 0
player2_score = 0
timer = 0

#Musicas
Naruto = "Naruto.mp3"
J3 = "J3.mp3"

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

#Definindo Fonte
font_name = pygame.font.match_font('arial')

#Criando objetos
bola = Bola(WIDTH/2 ,HEIGHT/2,20)
player1 = Jogador(WIDTH*1/3,player1_img,0)
player2 = Jogador(WIDTH*2/3,player2_img,1)
campo_futebol = Campo(0,HEIGHT - 30,WIDTH,30)
trave1 = Trave_1()
trave2 = Trave_2()

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
