#Funções
import pygame, math, classes
from os import path
from variaveis import *
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def mensagem_na_tela(msg,cor):
    tela_mensagem = font.render(msg, True, cor)
    pygame.draw.rect(tela, cor_branca, [tela_x/2-50,tela_y/2-50,150,100])
    tela.blit(tela_mensagem, [tela_x/2 - 30, tela_y/2])

def gameLoop():
	#Score
	player1_score = 0
	player2_score = 0
	# FPS
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
    # Update do Sprite
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

def gameEvents():
	#Colisão Player1
    if bateu:
        player1.pos.y = bateu[0].rect.top + 1
        player1.vel.y = 0

    #Colisão Player2
    if bateu_2:
        player2.pos.y = bateu_2[0].rect.top + 1
        player2.vel.y = 0

    #Colisão entre Players
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
            
    #Colisão entre Player - Trave
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
        player2_score += 1
        if bola.pos.y + bola.radius <= trave1.rect.top and bola.vel.y > 0:
            bola.vel.y = -bola.vel.y
        if bola.pos.y - bola.radius <= trave1.rect.top:
            bola.vel.y = -bola.vel.y
            #player2_score += 1
        if bola.pos.y + bola.radius > trave1.rect.bottom:
            player2_score += 1

    #Colisão entre Bola - Trave
    if bateu_bola_trave_2:
        player1_score += 1
        if bola.pos.y + bola.radius <= trave2.rect.top and bola.vel.y > 0:
            bola.vel.y = -bola.vel.y
        if bola.pos.y - bola.radius <= trave2.rect.top:
            bola.vel.y = -bola.vel.y
            player1_score += 1

    #Sprite Collide da bola - player
    colisao = pygame.sprite.spritecollide(bola,todos_jogadores,False,pygame.sprite.collide_circle)
    if colisao:
        bola.collide(colisao[0])

def gameDraw():
	 # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)

    # Desenha e Flipa
    screen.blit(font.render("fps: " + str(clock.get_fps()), 1, WHITE), (0,0))
    draw_text(screen,":", 40, WIDTH/2 - 20, 10)
    draw_text(screen,str(player1_score), 40, WIDTH/2 - 40, 10)
    draw_text(screen,str(player2_score), 40, WIDTH/2 + 2, 10)
    all_sprites.draw(screen) 
    pygame.display.flip()

def gameQuit():
	pygame.quit()
	quit()