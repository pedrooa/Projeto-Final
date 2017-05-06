import pygame
import random
import os

#Cores
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#Folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "Imagens")


class Bola(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#Carrega a img da bola
		self.image = pygame.image.load(os.path.join(img_folder, 'Ball2.jpg')).convert()
		#Retira as cores de fora da imagem da bola
		self.image.set_colorkey(black)
		#Cria um retangulo de colisão 
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
		self.y_speed = 5
		
	def update(self):
		self.rect.x += 5
		self.rect.y += self.y_speed
		if self.rect.bottom > HEIGHT - 250:
			self.y_speed = -5
		if self.rect.top < 100:
			self.y_speed = 5
		if self.rect.left > WIDTH:
			self.rect.right = 0

#Cria uma janela e declara variaveis
bg = pygame.image.load('C:\\Users\\vitor\\Dropbox\\Insper\\DesSoft\\Projeto Final HeadSoccer\\Projeto-Final\\Imagens\\background2.jpeg')
ball = pygame.image.load('C:\\Users\\vitor\\Dropbox\\Insper\\DesSoft\\Projeto Final HeadSoccer\\Projeto-Final\\Imagens\\SoccerBall.png')
WIDTH = 876
HEIGHT = 573
FPS = 30
pygame.init()
tela = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Head Soccer Game')
relogio = pygame.time.Clock()
running = True

#Sprites
all_sprites = pygame.sprite.Group()
bola = Bola()
all_sprites.add(bola)
#Loop do jogo
while running:
	#FPS da tela
	relogio.tick(FPS)
	#Analise de eventos
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


	#Desenhar e renderizar
	tela.fill(red)
	bola.update()
	all_sprites.draw(tela)
	#Update na tela
	pygame.display.update()

pygame.quit()