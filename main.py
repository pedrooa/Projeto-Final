#Head Soccer Game - Vitor, Gabriel, Pedro e Manzanna
#Programa main que rodará tudo
import pygame
import sys
import os
import time
vec = pygame.math.Vector2
current_path = os.getcwd()
print(current_path)
sys.path.insert(0, os.path.join(current_path, "../pymunk-4.0.0"))
pygame.init()
pygame.mixer.init()


#configuracoes
bola_x = 438
bola_y = 513
tela_x = 876
tela_y = 573

acc_jogador = 0.5
atrito_jogador = -0.12
gravidade_jogador = 0.8
cor_azul = (0,0,255)
cor_verde = (0,128,0)
cor_vermelha = (255,0,0)
cor_branca = (255,255,255)

FPS = 70

bg = pygame.image.load('Imagens/background2.jpeg')
tela = pygame.display.set_mode([tela_x, tela_y])
pygame.display.set_caption('Head Soccer Game')
relogio = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)


def mensagem_na_tela(msg,cor):
    tela_mensagem = font.render(msg, True, cor)
    pygame.draw.rect(tela, cor_branca, [tela_x/2-50,tela_y/2-50,150,100])
    tela.blit(tela_mensagem, [tela_x/2 - 30, tela_y/2])

class Jogador(pygame.sprite.Sprite):
    
    def __init__(self,x,cor,teclas):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = tela_y - 20
        self.pos = vec(x,self.rect.centery)
        self.vel = vec(0,0)
        self.acc = vec(0,0)  
        self.teclas = teclas

    def jump(self):
        # so pula se em cima de uma plataforma

        self.vel.y = -20

    def update(self):
        self.acc = vec(0,gravidade_jogador)
        keystate = pygame.key.get_pressed()
        if self.teclas == 0:
            if keystate[pygame.K_LEFT]:
                self.acc.x = -acc_jogador
            if keystate[pygame.K_RIGHT]:
                self.acc.x = acc_jogador
        elif self.teclas == 1:
            if keystate[pygame.K_a]:
                self.acc.x = -acc_jogador
            if keystate[pygame.K_d]:
                self.acc.x = acc_jogador
            
        
        
        #adiciona atrito
        self.acc.x += self.vel.x * atrito_jogador
        #equacoes do movimento
        self.vel += self.acc
        self.pos +=self.vel + acc_jogador * self.acc
        #nao deixa o jogador sair da tela
        if self.pos.x > tela_x:
            self.pos.x = tela_x
        if self.pos.x < 0:
            self.pos.x = 0

        self.rect.midbottom = self.pos

class Chao(pygame.sprite.Sprite):
    def __init__(self,x,y,l,a):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((l,a))
        self.image.fill(cor_verde)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y\


#Criar grupos de sprites
todos_sprites = pygame.sprite.Group()
todas_plataformas = pygame.sprite.Group()
todos_jogadores = pygame.sprite.Group()
jogador1 = Jogador(tela_x*2/3,cor_azul,0)
jogador2 = Jogador(tela_x*1/3,cor_vermelha,1)
chao = Chao(0,tela_y-40,tela_x,40)
todos_sprites.add(chao)
todos_sprites.add(jogador1)
todos_sprites.add(jogador2)
todas_plataformas.add(chao)
todos_jogadores.add(jogador1)
todos_jogadores.add(jogador2)

# Loop do jogo
def jogo_loop():

    pygame.mixer.music.load('HitBall.bfxrsound')
    pygame.mixer.music.play(-1,0.0)

    bola_x = 438
    bola_y = 513
    bola_raio = 30
    bola_x_change = 0
    bola_y_change = 0
    sair = False
    gameover = False


    while not sair:
        
        #Roda em x FPS
        relogio.tick(FPS)

        while gameover == True:
            #Tela inicial - nao funcionado
            tela.fill(cor_branca)
            mensagem_na_tela("Game Over, pressione C para jogar novamente ou Q para sair.")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_Q:
                        sair = True
                        gameover = False
                    elif event.key == pygame.K_C:
                        jogo_loop()
        
        for event in pygame.event.get():
            #checa se fechou a tela
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jogador1.jump()
                if event.key == pygame.K_w:
                    jogador2.jump()


        #Update
        todos_sprites.update()

        #Checa se os jogadores colidiram com a plataforma
        hits = pygame.sprite.spritecollide(jogador1, todas_plataformas, False)
        if hits:
            jogador1.pos.y= hits[0].rect.top + 1
            jogador1.vel.y = 0
        
        hits = pygame.sprite.spritecollide(jogador2, todas_plataformas, False)
        if hits:
            jogador2.pos.y= hits[0].rect.top + 1
            jogador2.vel.y = 0

        #Desenho/Renderizacao
        tela.fill(cor_verde)
        tela.blit(bg,(0,0,300,300))
        todos_sprites.draw(tela)

        #Depois de desenhar tudo, dar flip no display
        pygame.display.flip()

    #Fecha a janela e finaliza o jogo
    pygame.quit()



jogo_loop()
