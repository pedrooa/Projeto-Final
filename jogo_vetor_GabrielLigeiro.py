# Pygame template - skeleton for a new pygame project
import pygame
import math
from os import path
vetor = pygame.math.Vector2

WIDTH = 876
HEIGHT = 573
FPS = 60
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#configuracoes jogador
aceleração_maxima = 0.9
atrito = -0.12
gravidade = 0.7

#configuracoes bola
arrasto = 0.999
elasticidade = 0.75
gravidade_bola = 0.2
atrito_bola = - 0.10

class Bola(pygame.sprite.Sprite):
    def __init__(self,x,y,raio):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(SoccerBall, (34,34))
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.radius = int(raio)
        self.rect.centerx = x
        self.rect.centery = y
        self.pos = vetor(x,self.rect.centery)
        self.vel = vetor(0,0)
        self.acc = vetor(0,0)

    def update(self):
        self.acc = vetor(0,0.1)
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

        tangent = math.atan2(dy,dx)
        newvel = self.vel
        newvel = newvel.rotate(-tangent)
        newvel.x = -newvel.x
        newvel.y = -newvel.y
        self.vel = newvel*elasticidade
        self.vel += 2*other.vel*elasticidade
        self.vel.rotate(tangent)

class Jogador(pygame.sprite.Sprite):
    def __init__(self,x,imagem,teclas):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(imagem, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 24
       #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.center = (x, HEIGHT - 50)
        self.pos = vetor(x, self.rect.centery)
        self.vel = vetor(0, 0)
        self.acc = vetor(0, 0)
        self.teclas = teclas

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
        self.mask = pygame.mask.from_surface(self.image)

class Campo(pygame.sprite.Sprite):
    def __init__(self, x , y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Head Soccer pre-pre-pre-Alpha")
clock = pygame.time.Clock()

#carregando Imagens

game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, "Imagens")
background = pygame.image.load(path.join(img_folder, 'background2.jpeg')).convert()
background_rect = background.get_rect()
player1_img = pygame.image.load(path.join(img_folder, "cabeca1.png")).convert()
player2_img = pygame.image.load(path.join(img_folder, "cabeca2.png")).convert()
SoccerBall = pygame.image.load(path.join(img_folder, "SoccerBall.png")).convert()

#Sprites
all_sprites = pygame.sprite.Group()
plataformas = pygame.sprite.Group()
player2_group = pygame.sprite.Group()
player1_group = pygame.sprite.Group()
todos_jogadores = pygame.sprite.Group()

bola = Bola(WIDTH/2,HEIGHT/2,17)
player1 = Jogador(WIDTH*1/3,player1_img,0)
player2 = Jogador(WIDTH*2/3,player2_img,1)
campo_futebol = Campo(0,HEIGHT - 30,WIDTH,30)

#Adiciona os sprites
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(bola)
all_sprites.add(campo_futebol)
plataformas.add(campo_futebol)
player2_group.add(player2)
player1_group.add(player1)
todos_jogadores.add(player1)
todos_jogadores.add(player2)
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.jump()
            if event.key == pygame.K_UP:
                player2.jump()
    # Update
    all_sprites.update()

    #colisao entre jogadores e o campo
    bateu = pygame.sprite.spritecollide(player1, plataformas, False)
    bateu_2 = pygame.sprite.spritecollide(player2, plataformas, False)

    #colisao entre players
    bateu_player1_2 = pygame.sprite.spritecollide(player1, player2_group, False)
    bateu_player2_1 = pygame.sprite.spritecollide(player2, player1_group, False)
    if bateu:
        player1.pos.y = bateu[0].rect.top
        player1.vel.y = 0

    if bateu_2:
        player2.pos.y = bateu_2[0].rect.top
        player2.vel.y = 0
    if bateu_player1_2 and bateu_player2_1:
        player1.vel.x = 0
        player2.vel.x = 0
        player1.acc.x = 0
        player2.acc.x = 0
        if player1.pos.x < player2.pos.x:

            player2.pos.x  = bateu_player1_2[0].rect.left + 28
            player1.pos.x  = bateu_player2_1[0].rect.right - 28
        elif player1.pos.x < player2.pos.x:
            player2.pos.x  = bateu_player1_2[0].rect.right - 40
            player1.pos.x  = bateu_player2_1[0].rect.left + 40

    #Colisao da bola com os jogadores
    colisao = pygame.sprite.spritecollide(bola,todos_jogadores,False,pygame.sprite.collide_circle)
    if colisao:
        bola.collide(colisao[0])

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen) #rodando os sprites
    #pygame.draw.rect(screen, GREEN, [0,HEIGHT - 30,WIDTH,30])
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
