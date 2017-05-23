# Pygame template - skeleton for a new pygame project
import pygame
import math
from os import path
from settings import *

#funções
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
def playMusicJ3():
    pygame.mixer.music.load("J3.mp3")
    pygame.mixer.music.play(-1, 0.0)
def playMusicNaruto():
    pygame.mixer.music.load("Naruto.mp3")
    pygame.mixer.music.play(-1, 0.0)

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

#Sprites
all_sprites = pygame.sprite.Group()
plataformas = pygame.sprite.Group()
player2_group = pygame.sprite.Group()
player1_group = pygame.sprite.Group()
todos_jogadores = pygame.sprite.Group()
trave_1_group = pygame.sprite.Group()
trave_2_group = pygame.sprite.Group()

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

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)

    # Update
    all_sprites.update()

    #colisao dentro entre jogador campo
    bateu = pygame.sprite.spritecollide(player1, plataformas, False)
    bateu_2 = pygame.sprite.spritecollide(player2, plataformas, False)

    #colisao entre players
    bateu_player1_2 = pygame.sprite.spritecollide(player1, player2_group, False)
    bateu_player2_1 = pygame.sprite.spritecollide(player2, player1_group, False)
    bateu_trave1 = pygame.sprite.spritecollide(player1, trave_1_group, False)
    bateu_trave2 = pygame.sprite.spritecollide(player2, trave_2_group, False)
    bateu_bola_trave_1 = pygame.sprite.spritecollide(bola, trave_1_group, False)
    bateu_bola_trave_2 = pygame.sprite.spritecollide(bola, trave_2_group, False)
    if bateu:
        player1.pos.y = bateu[0].rect.top + 1
        player1.vel.y = 0

    if bateu_2:
        player2.pos.y = bateu_2[0].rect.top + 1
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
        if player1.pos.y < player2.pos.y:
            player1.pos.y = player2.rect.top + 2
            player1.vel.y = 0

    if bateu_trave1:
        if player1.pos.y -  10 <= trave1.rect.top and player1.vel.y  > 0:
            player1.pos.y = trave1.rect.top + 2
            player1.vel.y = 0
        if player1.pos.y - 60 <= trave1.rect.top:
            player1.vel.y = 0
            player1.vel.y = 5
    if bateu_trave2:
        if player2.pos.y -  10 <= trave2.rect.top and player2.vel.y  > 0:
            player2.pos.y = trave2.rect.top + 2
            player2.vel.y = 0
        if player2.pos.y - 60 <= trave2.rect.top:
            player2.vel.y = 0
            player2.vel.y = 5
    if bateu_bola_trave_1:
        if bola.pos.y <= trave1.rect.top and bola.vel.y > 0:
            bola.vel.y = -bola.vel.y
        if bola.pos.y - bola.radius >= trave1.rect.top:
            bola.vel.y = -bola.vel.y
            timer += 1
            if timer == 5:
                player2_score += 1
                bola.pos.y = HEIGHT/2
                bola.pos.x = WIDTH/2
                bola.vel.x = 0
                bola.vel.y = 0
                player1.pos.x = WIDTH/3
                player2.pos.x = WIDTH * 2/3
                player1.vel.x = 0
                player1.vel.y = 0
                player2.vel.x = 0
                player2.vel.y = 0
                timer = 0

    if bateu_bola_trave_2:
        if bola.pos.y <= trave2.rect.top and bola.vel.y > 0:
            bola.vel.y = -bola.vel.y
        if bola.pos.y - bola.radius >= trave2.rect.top:
            bola.vel.y = -bola.vel.y
            timer += 1
            if timer == 5:
                player1_score += 1
                bola.pos.y = HEIGHT/2
                bola.pos.x = WIDTH/2
                bola.vel.x = 0
                bola.vel.y = 0
                player1.pos.x = WIDTH/3
                player2.pos.x = WIDTH * 2/3
                player1.vel.x = 0
                player1.vel.y = 0
                player2.vel.x = 0
                player2.vel.y = 0
                timer = 0
    #Colisao da bola com os jogadores
    colisao = pygame.sprite.spritecollide(bola,todos_jogadores,False,pygame.sprite.collide_circle)
    if colisao:
        bola.collide(colisao[0])

    #musica
 #   playMusicNaruto()

    if timer2 >= 60:
        break
