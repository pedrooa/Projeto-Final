#Head Soccer Game - Vitor, Gabriel, Pedro e Manzanna
#Programa main que rodará tudo
import pygame as pg
import math
import random
from os import path
from settings import *
from Sprites import *

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
        self.timer2 = pg.time.get_ticks()/1000

        #carregando Imagens
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, "Imagens")
        self.background = pg.image.load(path.join(img_folder, \
                                                'background2.jpeg')).convert()
        self.background_rect = self.background.get_rect()
        self.player1_img = pg.image.load(path.join(img_folder, \
                                                "cabeca1.png")).convert()
        self.player2_img = pg.image.load(path.join(img_folder, \
                                                "cabeca2.png")).convert()
        self.SoccerBall = pg.image.load(path.join(img_folder, \
                                                "SoccerBall.png")).convert()
        self.sombra_bola = pg.image.load(path.join(img_folder, \
                                                "ball_shadow.png")).convert()

        self.traves1 = []
        self.traves1_lista = ['trave_1.png','Trave_1_grande.png','Trave_1_pequena.png']
        for img in self.traves1_lista :
             self.traves1.append(pg.image.load(path.join(img_folder,img)).convert())

        self.traves2 = []
        self.traves2_lista = ['trave_2.png','Trave_2_grande.png','Trave_2_pequena.png']
        for img in self.traves2_lista :
             self.traves2.append(pg.image.load(path.join(img_folder,img)).convert())

        self.powerup_images = {}
        self.powerup_images['velocidade'] = pg.image.load(path.join(img_folder,'bolt_gold.png')).convert()
        self.powerup_images['crescer'] = pg.image.load(path.join(img_folder,'crescer.png')).convert()
        self.powerup_images['diminuir'] = pg.image.load(path.join(img_folder,'diminuir.png')).convert()

        #Criando objetos
        self.bola = Bola(WIDTH/2 ,HEIGHT/2,20,self.SoccerBall)
        self.player1 = Jogador(self,WIDTH*1/3,self.player1_img,0)
        self.player2 = Jogador(self,WIDTH*2/3,self.player2_img,1)
        self.campo_futebol = Campo(0,HEIGHT - 30,WIDTH,30)
        self.trave1 = Trave(self.traves1[0],2,HEIGHT - 145,self)
        self.trave2 = Trave(self.traves2[0],WIDTH - 60, HEIGHT - 145,self)
        self.sombra = Sombra(self,self.sombra_bola)

        #Sprite Groups
        self.all_sprites = pg.sprite.Group()
        self.plataformas = pg.sprite.Group()
        self.player2_group = pg.sprite.Group()
        self.player1_group = pg.sprite.Group()
        self.todos_jogadores = pg.sprite.Group()
        self.trave_1_group = pg.sprite.Group()
        self.trave_2_group = pg.sprite.Group()
        self.powerups = pg.sprite.Group()

        #Adicionando nos grupos de sprites
        self.all_sprites.add(self.player1)
        self.all_sprites.add(self.player2)
        self.all_sprites.add(self.bola)
        self.all_sprites.add(self.campo_futebol)
        self.all_sprites.add(self.trave1)
        self.all_sprites.add(self.trave2)
        self.plataformas.add(self.campo_futebol)
        self.player2_group.add(self.player2)
        self.player1_group.add(self.player1)
        self.trave_1_group.add(self.trave1)
        self.trave_2_group.add(self.trave2)
        self.todos_jogadores.add(self.player1)
        self.todos_jogadores.add(self.player2)
        self.all_sprites.add(self.sombra)

        self.poweruptime = pg.time.get_ticks()

        self.run()

    def run(self):
        #Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.colision()
            self.draw()
            if self.timer2 >= 60:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        #Game loop update
        self.all_sprites.update()

        #Aparecimento de powerups
        now = pg.time.get_ticks()
        if now - self.poweruptime > 5000:
            self.poweruptime = now
            poder = Powerup(self)
            self.all_sprites.add(poder)



    '''def playMusicJ3():
        pg.mixer.music.load(J3)
        pg.mixer.music.play(-1, 0.0)'''

    '''def playMusicNaruto():
        pg.mixer.music.load(Naruto)
        pg.mixer.music.play(-1, 0.0)'''

    def colision(self):
        #Colisao dentro entre jogador campo
        self.bateu = pg.sprite.spritecollide(self.player1, self.plataformas,\
                                                        False)
        self.bateu_2 = pg.sprite.spritecollide(self.player2, self.plataformas,\
                                                        False)

        #Colisao entre players
        self.bateu_player1_2 = pg.sprite.spritecollide(self.player1, \
                                                        self.player2_group, False)
        self.bateu_player2_1 = pg.sprite.spritecollide(self.player2, \
                                                        self.player1_group, False)
        self.bateu_trave1 = pg.sprite.spritecollide(self.player1, \
                                                        self.trave_1_group, False)
        self.bateu_trave2 = pg.sprite.spritecollide(self.player2, \
                                                        self.trave_2_group, False)
        self.bateu_bola_trave_1 = pg.sprite.spritecollide(self.bola, \
                                                        self.trave_1_group, False)
        self.bateu_bola_trave_2 = pg.sprite.spritecollide(self.bola, \
                                                        self.trave_2_group, False)

        #Se bater player1 com plataforma
        if self.bateu:
            self.player1.pos.y = self.bateu[0].rect.top + 1
            self.player1.vel.y = 0

        #Se bater player2 com plataforma
        if self.bateu_2:
            self.player2.pos.y = self.bateu_2[0].rect.top + 1
            self.player2.vel.y = 0

        #Se bater player 2/1 com player 1/2
        if self.bateu_player1_2 and self.bateu_player2_1:
            self.player1.vel.x = 0
            self.player2.vel.x = 0
            self.player1.acc.x = 0
            self.player2.acc.x = 0
            """self.player1.vel.y = 0
            self.player2.vel.y = 0
            self.player1.acc.y = 0
            self.player2.acc.y = 0"""

            dx = self.player1.rect.centerx - self.player2.rect.centerx
            dy = self.player2.rect.centery - self.player2.rect.centery

            dist = math.hypot(dx,dy)

            soma_raios = self.player1.radius + self.player2.radius
            v = vetor(self.player1.rect.centerx - self.player2.rect.centerx,self.player2.rect.centery - self.player2.rect.centery)
            v_metade = v*0.05

            self.player1.pos += v_metade
            self.player2.pos -= v_metade

        #Se bater na trave - player1
        if self.bateu_trave1:
            if self.player1.pos.y -  10 <= self.trave1.rect.top \
                                    and self.player1.vel.y  >  0:
                self.player1.pos.y = self.trave1.rect.top + 2
                self.player1.vel.y = 0
            if self.player1.pos.y - 60 <= self.trave1.rect.top:
                self.player1.vel.y = 0
                self.player1.vel.y = 5

        #Se bater na trave - player2
        if self.bateu_trave2:
            if self.player2.pos.y -  10 <= self.trave2.rect.top \
                                    and self.player2.vel.y  > 0:
                self.player2.pos.y = self.trave2.rect.top + 2
                self.player2.vel.y = 0
            if self.player2.pos.y - 60 <= self.trave2.rect.top:
                self.player2.vel.y = 0
                self.player2.vel.y = 5
        if self.bateu_bola_trave_1:
            if self.bola.pos.y <= self.trave1.rect.top and self.bola.vel.y > 0:
                self.bola.vel.y = -self.bola.vel.y
            if self.bola.pos.y - self.bola.radius >= self.trave1.rect.top:
                self.bola.vel.y = -self.bola.vel.y
                self.timer += 1
                if self.timer == 5:
                    self.player2_score += 1
                    self.bola.pos.y = HEIGHT/2
                    self.bola.pos.x = WIDTH/2
                    self.bola.vel.x = 0
                    self.bola.vel.y = 0
                    self.player1.pos.x = WIDTH/3
                    self.player2.pos.x = WIDTH * 2/3
                    self.player1.vel.x = 0
                    self.player1.vel.y = 0
                    self.player2.vel.x = 0
                    self.player2.vel.y = 0
                    self.timer = 0

        if self.bateu_bola_trave_2:
            if self.bola.pos.y <= self.trave2.rect.top and self.bola.vel.y > 0:
                self.bola.vel.y = -self.bola.vel.y
            if self.bola.pos.y - self.bola.radius >= self.trave2.rect.top:
                self.bola.vel.y = -self.bola.vel.y
                self.timer += 1
                if self.timer == 5:
                    self.player1_score += 1
                    self.bola.pos.y = HEIGHT/2
                    self.bola.pos.x = WIDTH/2
                    self.bola.vel.x = 0
                    self.bola.vel.y = 0
                    self.player1.pos.x = WIDTH/3
                    self.player2.pos.x = WIDTH * 2/3
                    self.player1.vel.x = 0
                    self.player1.vel.y = 0
                    self.player2.vel.x = 0
                    self.player2.vel.y = 0
                    self.timer = 0
        #Colisao da bola com os jogadores
        self.colisao = pg.sprite.spritecollide(self.bola,self.todos_jogadores,\
                                        False,pg.sprite.collide_circle)
        if self.colisao:
            self.bola.collide(self.colisao[0])

        #Checa se o jogador pegou um powerup
        hits = pg.sprite.spritecollide(self.player1,self.powerups,True)
        for hit in hits:
            pass

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
                    self.player1.jump()
                if event.key == pg.K_UP:
                    self.player2.jump()
                if event.key == pg.K_s:
                    self.player1.dash()
                if event.key == pg.K_DOWN:
                    self.player2.dash()

    def draw(self):
        #Game loop draw
        # Draw / render
        self.screen.fill(BLACK)
        self.screen.blit(self.background, self.background_rect)
        # Info and flip screen
        self.screen.blit(self.font.render("fps: " + str(self.clock.get_fps()), 1, WHITE), (0,0))
        self.draw_text(self.screen,":", 40, WIDTH/2 - 20,10)
        self.draw_text(self.screen,str(self.player1_score), 40, WIDTH/2 - 50, 10)
        self.draw_text(self.screen,str(self.player2_score), 40, WIDTH/2 + 10, 10)
        self.draw_text(self.screen,str(round(self.timer2,1)), 40, WIDTH*5/6, 10)
        self.all_sprites.draw(self.screen) #rodando os sprites

        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        #Game Start Screen
        pass

    def show_GO_screen(self):
        #Game Over show_GO_screen
        pass

    def draw_text(self,surf, text, size, x, y):
        font = self.font
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_GO_screen()

pg.quit()
