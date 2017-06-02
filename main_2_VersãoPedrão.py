
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
        self.font = pg.font.SysFont("Arial", 18)
        self.font_name = pg.font.match_font('arial')
        self.intro = True
        self.num = 0
        self.num1 = 0

    def new(self):
        #start a new game
        #SCORE e timers
        self.player1_score = 0
        self.player2_score = 0
        self.timer = 0

        #carregando Imagens
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, "Imagens")
        J3_folder = path.join(game_folder, "Musicas", 'J3.wav')
        Naruto_folder = path.join(game_folder, "Musicas", 'Naruto.wav')
        Ronaldo_folder = path.join(game_folder, "Musicas", 'Ronaldo.wav')
        Skank_folder = path.join(game_folder, "Musicas", 'Skank.wav')
        Nascido_folder = path.join(game_folder, "Musicas", 'Nascido.wav')
        Guime_folder = path.join(game_folder, "Musicas", 'Guime.wav')

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
             self.traves1.append(pg.image.load(path.join(img_folder,img)).convert_alpha())

        self.traves2 = []
        self.traves2_lista = ['trave_2.png','Trave_2_grande.png','Trave_2_pequena.png']
        for img in self.traves2_lista :
             self.traves2.append(pg.image.load(path.join(img_folder,img)).convert_alpha())

        self.jogadores_2 = []
        self.jogadores_lista_1 = ['cabeca1.png','cabeca2.png','bob.png','fabuloso.png','pizzi.png','ronalducho.png','rooney.png']
        for img in self.jogadores_lista_1:
            self.jogadores_2.append(pg.image.load(path.join(img_folder,img)).convert_alpha())

        self.jogadores_1 = []
        self.jogadores_lista_2 = ['cabeca1_2.png','cabeca2_2.png','bob_2.png','fabuloso_2.png','pizzi_2.png','ronalducho_2.png','rooney_2.png']
        for img in self.jogadores_lista_2:
            self.jogadores_1.append(pg.image.load(path.join(img_folder,img)).convert_alpha())

        self.powerup_images = {}
        self.powerup_images['velocidade'] = pg.image.load(path.join(img_folder,'bolt_gold.png')).convert()
        self.powerup_images['crescer'] = pg.image.load(path.join(img_folder,'crescer.png')).convert()
        self.powerup_images['diminuir'] = pg.image.load(path.join(img_folder,'diminuir.png')).convert()
        self.powerup_images['gelo'] = pg.image.load(path.join(img_folder,'gelo.jpeg')).convert()

        self.grass_2 = pg.image.load(path.join(img_folder, \
                                                "grass_2.png")).convert()

        #Colocando musicas
        musica = random.choice([J3_folder,Naruto_folder, Skank_folder, Ronaldo_folder, Nascido_folder])
        pg.mixer.music.load(musica)
        pg.mixer.music.play(-1)
        #Criando objetos
        self.bola = Bola(WIDTH/2 ,HEIGHT/2,11,self.SoccerBall)
        self.player1 = Jogador(self,WIDTH*1/3,self.jogadores_1[self.num],0)
        self.player2 = Jogador(self,WIDTH*2/3,self.jogadores_2[self.num1],1)
        self.campo_futebol = Campo(0,HEIGHT - 30,self.grass_2,WIDTH,30)
        self.trave1 = Trave(self.traves1,2,HEIGHT - 145,self)
        self.trave2 = Trave(self.traves2,WIDTH - 60, HEIGHT - 145,self)
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
        self.timer2 = pg.time.get_ticks()/1000 - self.timer_menu

        #Aparecimento de powerups
        now = pg.time.get_ticks()
        if now - self.poweruptime > 10000:
            self.poweruptime = now
            poder = Powerup(self)
            self.all_sprites.add(poder)
            self.powerups.add(poder)

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
            #if self.bateu or self.bateu_2:
            #    self.player1.vel.y = -1
            #    self.player2.vel.y = -1
            #    self.player1.acc.y = -1
            #    self.player2.acc.y = -1


            dx = self.player1.rect.centerx - self.player2.rect.centerx
            dy = self.player2.rect.centery - self.player2.rect.centery

            dist = math.hypot(dx,dy)
            soma_raios = self.player1.radius + self.player2.radius

            if self.bateu or self.bateu_2:
                v = vetor(dx, dy)
            else:
                v = vetor(dx, 0)

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
                self.player1.vel.y = 5

        #Se bater na trave - player2
        if self.bateu_trave2:
            if self.player2.pos.y -  10 <= self.trave2.rect.top \
                                    and self.player2.vel.y  > 0:
                self.player2.pos.y = self.trave2.rect.top + 2
                self.player2.vel.y = 0
            if self.player2.pos.y - 60 <= self.trave2.rect.top:
                self.player2.vel.y = 5

        # Se Bater Bola na Trave
        if self.bateu_bola_trave_1:
            if self.bola.pos.y + self.bola.radius >= self.trave1.rect.top \
            and self.bola.pos.x <= 67:
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
            if self.bola.pos.y + self.bola.radius >= self.trave2.rect.top\
            and self.bola.pos.x >= WIDTH - 63:
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

        #Checa se o jogador1 pegou um powerup
        self.hits = pg.sprite.spritecollide(self.player1,self.powerups,True)
        for hit in self.hits:
            if hit.type == 'crescer':
                self.trave2.powerup_1()
            if hit.type == 'diminuir':
                self.trave2.powerup_2()
            if hit.type == 'gelo':
                self.player1.powerup_gelo()
            if hit.type == 'raio':
                self.player1.powerup_raio()

        #Checa se o jogador2 pegou um powerup
        self.hits = pg.sprite.spritecollide(self.player2,self.powerups,True)
        for hit in self.hits:
            if hit.type == 'crescer':
                self.trave1.powerup_1()
            if hit.type == 'diminuir':
                self.trave1.powerup_2()
            if hit.type == 'gelo':
                self.player2.powerup_gelo()
            if hit.type == 'velocidade':
                self.player2.powerup_raio()

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
        self.screen.blit(self.font.render("fps: " + str(round(self.clock.get_fps())), 1, WHITE), (0,0))
        self.draw_text(self.screen,":", 70, WIDTH/2 ,10)
        self.draw_text(self.screen,str(self.player1_score), 70, WIDTH/2 - 30, 10)
        self.draw_text(self.screen,str(self.player2_score), 70, WIDTH/2 + 30, 10)
        self.draw_text(self.screen,str(round(self.timer2,1)), 50, WIDTH*5/6, 10)
        self.all_sprites.draw(self.screen) #rodando os sprites

        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, "Imagens")
        Guime_folder = path.join(game_folder, "Musicas", 'Guime.wav')
        pg.mixer.music.load(Guime_folder)
        pg.mixer.music.play(-1)

        self.fundo = pg.image.load(path.join(img_folder, "background1.JPG")).convert_alpha()
        self.titulo = pg.image.load(path.join(img_folder, "titulo.PNG")).convert_alpha() #imagem do titulo
        self.bright_play = pg.image.load(path.join(img_folder, "bright_play.PNG")).convert_alpha() # botão play com o mouse em cima
        self.play = pg.image.load(path.join(img_folder, "play.PNG")).convert_alpha() #botão play
        self.quit = pg.image.load(path.join(img_folder, "quit.PNG")).convert_alpha() #botão quit
        self.quit_bright = pg.image.load(path.join(img_folder, "quit_bright.PNG")).convert_alpha() #botão quit com o mouse em cima
        self.background1 = pg.transform.scale(self.fundo,(WIDTH,HEIGHT)) #fundo
        #menu
        self.background2 = self.background1.get_rect()
        self.background2.x = WIDTH/2
        self.background2.y = HEIGHT*2/3
        self.screen.blit(self.background1, self.background2)

        #Game Start Screen


        while self.intro:
            self.background2 = self.background1.get_rect()
            self.screen.blit(self.background1, self.background2)
            self.screen.blit(self.titulo, (WIDTH*1/7,0))
            self.button(self.play,128,360,170,66,self.bright_play,'play')
            self.button(self.quit,561,360,156,75,self.quit_bright,'quit')
            self.timer_menu = pg.time.get_ticks()/1000


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

            pg.display.update()


    def show_GO_screen(self):
        #Game Over show_GO_screen
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, "Imagens")
        #carregando as imagens
        self.play = pg.image.load(path.join(img_folder, "play.PNG")).convert_alpha() #botão play
        self.quit = pg.image.load(path.join(img_folder, "quit.PNG")).convert_alpha() #botão quit
        self.c1 = pg.image.load(path.join(img_folder, "cabeca1.png")).convert_alpha()
        self.c2 = pg.image.load(path.join(img_folder, "cabeca2.png")).convert_alpha()
        self.c3 = pg.image.load(path.join(img_folder, "bob.png")).convert_alpha()
        self.c4 = pg.image.load(path.join(img_folder, "fabuloso.png")).convert_alpha()
        self.c5 = pg.image.load(path.join(img_folder, "pizzi.png")).convert_alpha()
        self.c6 = pg.image.load(path.join(img_folder, "ronalducho.png")).convert_alpha()
        self.c7 = pg.image.load(path.join(img_folder, "rooney.png")).convert_alpha()
        self.c1n = pg.image.load(path.join(img_folder, "cabeca1_selecionado.png")).convert_alpha()
        self.c2n = pg.image.load(path.join(img_folder, "cabeca2_selecionado.png")).convert_alpha()
        self.c3n = pg.image.load(path.join(img_folder, "bob_selecionado.png")).convert_alpha()
        self.c4n = pg.image.load(path.join(img_folder, "fabuloso_selecionado.png")).convert_alpha()
        self.c5n = pg.image.load(path.join(img_folder, "pizzi_selecionado.png")).convert_alpha()
        self.c6n = pg.image.load(path.join(img_folder, "ronalducho_selecionado.png")).convert_alpha()
        self.c7n = pg.image.load(path.join(img_folder, "rooney_selecionado.png")).convert_alpha()
        self.c1e = pg.image.load(path.join(img_folder, "cabeca1_2.png")).convert_alpha()
        self.c2e = pg.image.load(path.join(img_folder, "cabeca2_2.png")).convert_alpha()
        self.c3e = pg.image.load(path.join(img_folder, "bob_2.png")).convert_alpha()
        self.c4e = pg.image.load(path.join(img_folder, "fabuloso_2.png")).convert_alpha()
        self.c5e = pg.image.load(path.join(img_folder, "pizzi_2.png")).convert_alpha()
        self.c6e = pg.image.load(path.join(img_folder, "ronalducho_2.png")).convert_alpha()
        self.c7e = pg.image.load(path.join(img_folder, "rooney_2.png")).convert_alpha()
        self.c1en = pg.image.load(path.join(img_folder, "cabeca1_selecionado2.png")).convert_alpha()
        self.c2en = pg.image.load(path.join(img_folder, "cabeca2_selecionado2.png")).convert_alpha()
        self.c3en = pg.image.load(path.join(img_folder, "bob_selecionado2.png")).convert_alpha()
        self.c4en = pg.image.load(path.join(img_folder, "fabuloso_selecionado2.png")).convert_alpha()
        self.c5en = pg.image.load(path.join(img_folder, "pizzi_selecionado2.png")).convert_alpha()
        self.c6en = pg.image.load(path.join(img_folder, "ronalducho_selecionado2.png")).convert_alpha()
        self.c7en = pg.image.load(path.join(img_folder, "rooney_selecionado2.png")).convert_alpha()
        self.fundo = pg.image.load(path.join(img_folder, "background1.JPG")).convert_alpha()

        self.background1 = pg.transform.scale(self.fundo,(WIDTH,HEIGHT)) #fundo
        #menu
        self.background2 = self.background1.get_rect()
        self.background2.x = WIDTH/2
        self.background2.y = HEIGHT*2/3
        self.screen.blit(self.background1, self.background2)

        #Game Start Screen
        verdade = True

        while verdade:
            self.background2 = self.background1.get_rect()
            self.screen.blit(self.background1, self.background2)
            self.screen.blit(self.titulo, (WIDTH*1/7,0))
            self.button(self.play,100,500,170,66,self.bright_play,'jogar')
            self.button(self.quit,500,500,1560,75,self.quit_bright,'quit')
            self.button(self.c1,500,250,60,60,self.c1n,'c1')
            self.button(self.c2,550,250,60,60,self.c2n,'c2')
            self.button(self.c3,600,250,60,60,self.c3n,'c3')
            self.button(self.c4,650,250,60,60,self.c4n,'c4')
            self.button(self.c5,500,300,60,60,self.c5n,'c5')
            self.button(self.c6,550,300,60,60,self.c6n,'c6')
            self.button(self.c7,600,300,60,60,self.c7n,'c7')
            self.button(self.c1e,100,250,60,60,self.c1en,'c1e')
            self.button(self.c2e,150,250,60,60,self.c2en,'c2e')
            self.button(self.c3e,200,250,60,60,self.c3en,'c3e')
            self.button(self.c4e,250,250,60,60,self.c4en,'c4e')
            self.button(self.c5e,100,300,60,60,self.c5en,'c5e')
            self.button(self.c6e,150,300,60,60,self.c6en,'c6e')
            self.button(self.c7e,200,300,60,60,self.c7en,'c7e')
            self.timer_menu = pg.time.get_ticks()/1000


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            pg.display.update()


    def draw_text(self,surf, text, size, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def button(self,img, x, y, width, height, img1, action = None):
        self.cur = pg.mouse.get_pos()
        self.click = pg.mouse.get_pressed()
        self.screen.blit (img, (x,y))
        if x+width > self.cur[0] > x and y+height > self.cur[1] > y:
            self.screen.blit(img, (x,y))
            if self.click[0] == 1 and action != None:

                #se der tempo/ nao tiver funcionando colocar na função menu

                if action == "play":
                    self.intro = False
                    print(1)
                    self.show_GO_screen()



                elif action == "quit":
                    pg.quit()
                    quit()


                elif action == "jogar":
                    print(2)
                    self.new()
                elif action == "c1":
                    self.num = 0
                elif action == "c2":
                    self.num = 1
                elif action == "c3":
                    self.num = 2
                elif action == "c4":
                    self.num = 3
                elif action == "c5":
                    self.num = 4
                elif action == "c6":
                    self.num = 5
                elif action == "c7":
                    self.num = 6
                elif action == "c1e":
                    self.num1 = 0
                elif action == "c2e":
                    self.num1 = 1
                elif action == "c3e":
                    self.num1 = 2
                elif action == "c4e":
                    self.num1 = 3
                elif action == "c5e":
                    self.num1 = 4
                elif action == "c6e":
                    self.num1 = 5
                elif action == "c7e":
                    self.num1 = 6
        else:
            self.screen.blit(img1, (x,y))

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_GO_screen()

pg.quit()
