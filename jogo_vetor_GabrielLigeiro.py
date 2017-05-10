# Pygame template - skeleton for a new pygame project
import pygame
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

#setting para a movimentacao com vetor
aceleração_maxima = 0.9
atrito = -0.12
gravidade = 0.7

class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(SoccerBall, (40,40))
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.radius = 19
        self.rect.center = (WIDTH / 2, 250)
        self.pos = vetor(WIDTH / 2, 250)
        self.vel = vetor(0, 0)
        self.acc = vetor(0, 0)

    def update(self):
        self.acc = vetor(0, gravidade)

        self.vel += self.acc
        self.pos += self.vel + 0.5 *self.acc

        #Final da tela
        if self.pos.x + 25 > WIDTH:
            self.pos.x = WIDTH - 25
        if self.pos.x - 25 < 0:
            self.pos.x =  25
        self.rect.midbottom = self.pos

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player1_img, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
       # self.radius = 24
       # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.center = (WIDTH /10, HEIGHT - 50)
        self.pos = vetor(WIDTH / 10, HEIGHT-50)
        self.vel = vetor(0, 0)
        self.acc = vetor(0, 0)
        
    def jump(self):
        self.rect.y += 1 
        hits = pygame.sprite.spritecollide(self, plataformas, False)
        self.rect.y -= 1 
        if hits:
            self.vel.y = -15


        
    def update(self):
        self.acc = vetor(0, gravidade)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.acc.x = -aceleração_maxima
        if keystate[pygame.K_d]:
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
            
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player2_img, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
       #self.radius = 24 #melhora no espaco fisico do jogador
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius) #para ver como o raio do jogador esta
        self.rect.center = (WIDTH * 9/10, HEIGHT - 50)
        self.pos = vetor(WIDTH * 9/10, HEIGHT-50)
        self.vel = vetor(0, 0)
        self.acc = vetor(0, 0)

    def jump(self):
        self.rect.x += 1 
        hits = pygame.sprite.spritecollide(self, plataformas, False)
        self.rect.x -= 1 
        if hits:
            self.vel.y = -15


    def update(self):
        self.acc = vetor(0, gravidade)
        keystate = pygame.key.get_pressed()
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
bola = Bola()
player1 = Player1()
player2 = Player2()


campo_futebol = Campo(0,HEIGHT - 30,WIDTH,30)
all_sprites.add(player1) #ADD Sprites
all_sprites.add(player2)
all_sprites.add(bola)
all_sprites.add(campo_futebol)
plataformas.add(campo_futebol)
player2_group.add(player2)
player1_group.add(player1)
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
        #colisao dentro entre jogador campo
    bateu = pygame.sprite.spritecollide(player1, plataformas, False)
    bateu_2 = pygame.sprite.spritecollide(player2, plataformas, False)
    bateu_bola = pygame.sprite.spritecollide(bola, plataformas, False)
    #colisao entre players
    bateu_player1_2 = pygame.sprite.spritecollide(player1, player2_group, False)
    bateu_player2_1 = pygame.sprite.spritecollide(player2, player1_group, False)
    if bateu:
        player1.pos.y = bateu[0].rect.top
        player1.vel.y = 0
        
    if bateu_2:
        player2.pos.y = bateu_2[0].rect.top
        player2.vel.y = 0
    if bateu_bola:
        bola.pos.y = bateu_bola[0].rect.top
        bola.vel.y = 0
    if bateu_player1_2 and bateu_player2_1:
        player1.vel.x = 0
        player2.vel.x = 0
        player1.acc.x = 0
        player2.acc.x = 0
        if player1.pos.x < player2.pos.y:

            player2.pos.x  = bateu_player1_2[0].rect.left + 28
            player1.pos.x  = bateu_player2_1[0].rect.right - 28
        elif player1.pos.x < player2.pos.y:
            player2.pos.x  = bateu_player1_2[0].rect.right - 40
            player1.pos.x  = bateu_player2_1[0].rect.left + 40

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen) #rodando os sprites
    #pygame.draw.rect(screen, GREEN, [0,HEIGHT - 30,WIDTH,30])
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
