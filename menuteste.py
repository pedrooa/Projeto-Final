import pygame as pg 
import random
from main import *


TITLE = "BOLUDOS FC"
FONT_NAME = "Arial"
WIDHT = 876
HEIGHT = 573
GREEN = (0, 200, 0)



class Game():
	def __init__(self):
		#iniciando a janela do jogo, etc
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((876, 573))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()	
		self.running = True
		self.font_name = pg.font.match_font(FONT_NAME)

	def mensagem_na_tela(msg,cor):
    tela_mensagem = font.render(msg, True, cor)
    pygame.draw.rect(tela, cor_branca, [tela_x/2-50,tela_y/2-50,150,100])
    tela.blit(tela_mensagem, [tela_x/2 - 30, tela_y/2])


	def show_start_screen(self):
			#start menu
		self.screen.fill((0, 200, 0))
		self.screen.mensagem_na_tela(TITLE, 48, GREEN, WIDTH / 2, HEIGHT / 4)
		self.screen.mensagem_na_tela('Setinhas movem o p1, "W", "S", "D", "A" movem o p2',22, [GREEN, WIDTH / 2, HEIGHT / 2])
		self.screen.mensagem_na_tela('Aperte qualquer botão para jogar', 22, [GREEN, WIDTH / 2, HEIGHT *3/4])
		pg.display.flip()
		self.wait_for_key()

	def wait_for_key(self):
		waiting = True
		while  waiting:
			self.clock.tick(FPS)
			for event in pg.event.get():
				if event.type == pg.QUIT:
					waiting = False
					self.running = False
				if event.type == pg.KEYUP:
					waiting = False

				


	def show_go_screen(self):
		#game over/continue
		if not self.running:
			return	
		self.screen.fill('green')
		self.screen.mensagem_na_tela('game over', 48)
		self.screen.mensagem_na_tela('IAMGINE O PLACAR',22)
		self.screen.mensagem_na_tela('Aperte qualquer botão para jogar de novo', 22)
		pg.display.flip()
		self.wait_for_key()

g = Game()
g.show_start_screen()
while g.running:
	g.show_go_screen()