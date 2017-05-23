import pygame as pg
import math
from os import path
from settings import *

class Trave_1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(trave_1, (TRAVE_W,TRAVE_H))
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 2
        self.rect.y = HEIGHT - 145

class Trave_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(trave_2, (TRAVE_W,TRAVE_H))
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()

        self.rect.x = WIDTH - 60
        self.rect.y = HEIGHT - 145

class Bola(pygame.sprite.Sprite):
    def __init__(self,x,y,raio):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(SoccerBall, (BOLA_W,BOLA_H))
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.radius = int(raio)
        self.rect.centerx = x
        self.rect.centery = y
        self.pos = vetor(x,self.rect.centery)
        self.vel = vetor(0,0)
        self.acc = vetor(0,0)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.acc = vetor(0,0.4)
        self.quicar()
        self.vel*= arrasto
        self.vel += self.acc
        self.pos += self.vel

        self.rect.center = self.pos

    #Bola quica na tela
    def quicar(self):
        if self.pos.x > WIDTH - self.radius:
            self.pos.x = 2*(WIDTH - self.radius) - self.pos.x
            self.vel.x = -self.vel.x
            self.vel*= elasticidade

        elif self.pos.x < self.radius:
            self.pos.x = 2*self.radius - self.pos.x
            self.vel.x = -self.vel.x
            self.vel*=elasticidade

        if self.pos.y > HEIGHT-30 - self.radius:
            self.pos.y = 2*(HEIGHT-30 - self.radius) - self.pos.y
            self.vel.y = -self.vel.y
            self.vel*=elasticidade

        elif self.pos.y < self.radius:
            self.pos.y = 2*self.radius - self.pos.y
            self.vel.y = -self.vel.y
            self.vel*=elasticidade

    def collide(self,other):
        dx = self.rect.x - other.rect.x
        dy = self.rect.y - other.rect.y

        dist = math.hypot(dx,dy)
        soma_raios = self.radius + other.radius
        if dist < soma_raios:
            force = 3*(soma_raios - dist)
            v = vetor(other.rect.x-self.rect.x,other.rect.y-self.rect.y)
            versor = v/dist
            FEL = force*versor
            self.vel -= 0.12*FEL

class Jogador(pygame.sprite.Sprite):
    def __init__(self,x,imagem,teclas):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(imagem, (PLAYER_W, PLAYER_H))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = PLAYER_RAIO
       #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.center = (x, HEIGHT - PLAYER_H)
        self.pos = vetor(x, self.rect.centery)
        self.vel = vetor(0, 0)
        self.acc = vetor(0, 0)
        self.teclas = teclas
        self.mask = pygame.mask.from_surface(self.image)

    def jump(self):
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, plataformas, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -15

    def update(self):
        self.acc = vetor(0, gravidade)
        keystate = pygame.key.get_pressed()
        if self.teclas == 0:
            if keystate[pygame.K_a]:
                self.acc.x = -aceleração_maxima
            if keystate[pygame.K_d]:
                self.acc.x = aceleração_maxima
        elif self.teclas ==1:

            if keystate[pygame.K_LEFT]:
                self.acc.x = -aceleração_maxima
            if keystate[pygame.K_RIGHT]:
                self.acc.x = aceleração_maxima

       #aplicando atrito
        self.acc.x += self.vel.x *  atrito
        #equacao de movimento
        self.vel += self.acc
        self.pos += self.vel + 0.5 *self.acc

        #bater na parede
        if self.pos.x + 25 > WIDTH:
            self.pos.x = WIDTH - 25
        if self.pos.x - 25 < 0:
            self.pos.x =  25
        self.rect.midbottom = self.pos

    def dash(self):
        self.vel.x = self.vel.x * 4

class Campo(pygame.sprite.Sprite):
    def __init__(self, x , y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Game:
	def __init__(self):
		#inicializa game window, etc
		self.running = True
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg.display.set_caption("Head Soccer pre-pre-pre-Alpha")
		self.clock = pg.time.Clock()
		self.font = pg.font.SysFont("Arial", 16)

	def new(self):
		#start a new game
		#SCORE e timers
		self.player1_score = 0
		self.player2_score = 0
		self.timer = 0
		self.timer2 = pygame.time.get_ticks()/1000
		#carregando Imagens
		game_folder = path.dirname(__file__)
		img_folder = path.join(game_folder, "Imagens")
		self.background = pygame.image.load(path.join(img_folder, 'background2.jpeg')).convert()
		background_rect = self.background.get_rect()
		self.player1_img = pygame.image.load(path.join(img_folder, "cabeca1.png")).convert()
		self.player2_img = pygame.image.load(path.join(img_folder, "cabeca2.png")).convert()
		self.SoccerBall = pygame.image.load(path.join(img_folder, "SoccerBall.png")).convert()
		self.trave_1 = pygame.image.load(path.join(img_folder, "trave_1.png")).convert()
		self.trave_2 = pygame.image.load(path.join(img_folder, "trave_2.png")).convert()
		#Sprite Groups
		self.all_sprites = pg.sprite.Group()
		self.plataformas = pg.sprite.Group()
		self.player2_group = pg.sprite.Group()
		self.player1_group = pg.sprite.Group()
		self.todos_jogadores = pg.sprite.Group()
		self.trave_1_group = pg.sprite.Group()
		self.trave_2_group = pg.sprite.Group()

	def run(self):
		#Game loop
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()
			self.finish()
		pass

	def update(self):
		#Game loop update
		self.all_sprites.update()

	def events(self):
		#Game loop events
	    for event in pg.event.get():
	        # check for closing window
	        if event.type == pg.QUIT:
				if self.playing:
					self.playing = False
				self.running = False
	        if event.type == pg.KEYDOWN:
	            if event.key == pg.K_w:
	                player1.jump()
	            if event.key == pg.K_UP:
	                player2.jump()
	            if event.key == pg.K_s:
	                player1.dash()
	            if event.key == pg.K_DOWN:
	                player2.dash()
	def draw(self):
		#Game loop draw
		# Draw / render
	    self.screen.fill(BLACK)
	    self.screen.blit(background, background_rect)
	    # Info and flip screen
	    self.screen.blit(font.render("fps: " + str(clock.get_fps()), 1, WHITE), (0,0))
	    draw_text(screen,":", 40, WIDTH/2 - 20, 10)
	    draw_text(screen,str(player1_score), 40, WIDTH/2 - 50, 10)
	    draw_text(screen,str(player2_score), 40, WIDTH/2 + 10, 10)
	    draw_text(screen,str(round(timer2,1)), 40, WIDTH*5/6, 10)
	    self.all_sprites.draw(screen) #rodando os sprites

	    # *after* drawing everything, flip the display
	    pg.display.flip()
		pass

	def show_start_screen(self):
		#Game Start Screen
		pass

	def show_GO_screen(self):
		#Game Over show_GO_screen
		pass

g = Game()
g.show_start_screen()
while g.running:
	g.new()
	g.show_GO_screen()

pg.quit()
