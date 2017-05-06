#Head Soccer Game - Vitor, Gabriel, Pedro e Manzanna
#Programa main que rodará tudo
import pygame
import time

pygame.init()

bola_x = 438
bola_y = 513
tela_x = 876
tela_y = 573
cor_verde = (0,128,0)
cor_vermelha = (255,0,0)
cor_branca = (255,255,255)
FPS = 70

bg = pygame.image.load('C:\\Users\\vitor\\Dropbox\\Insper\\DesSoft\\Projeto Final HeadSoccer\\Projeto-Final\\Imagens\\background2.jpeg')
tela = pygame.display.set_mode([tela_x, tela_y])
pygame.display.set_caption('Head Soccer Game')
relogio = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

def mensagem_na_tela(msg,cor):
    tela_mensagem = font.render(msg, True, cor)
    pygame.draw.rect(tela, cor_branca, [tela_x/2-50,tela_y/2-50,150,100])
    tela.blit(tela_mensagem, [tela_x/2 - 30, tela_y/2])

def jogo_loop():
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
            tela.fill(cor_branca)
            mensagem_na_tela("Game Over, pressione C para jogar novamente ou Q para sair.")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sair = True
                        gameover = False
                    elif event.key == pygame.K_c:
                        jogo_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    bola_x_change = -5
                    bola_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    bola_x_change = 5
                    bola_y_change = 0
                elif event.key == pygame.K_UP:
                    bola_y_change = -5
                    bola_x_change = 0
                elif event.key == pygame.K_DOWN:
                    bola_y_change = 5
                    bola_x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    bola_x_change = 0
                    bola_y_change = 0

        #Quando atingir as bordas fecha o jogo
        if bola_x <= 30 or bola_x >= tela_x - 30 or bola_y <= 30 or bola_y >= tela_y - 59:
            gameOver = True

        #Movimentação contínua
        bola_x += bola_x_change
        bola_y += bola_y_change
        
        #Tela
        tela.fill(cor_verde)
        tela.blit(bg,(0,0,300,300))
        #Simulando campo, trave e bola
        pygame.draw.circle(tela, cor_branca, [bola_x, bola_y], bola_raio)
        pygame.draw.rect(tela, cor_branca, [tela_x - 100,tela_y - 100,20,100])
        pygame.draw.rect(tela, cor_branca, [tela_x - 700,tela_y - 100,20,100])
        pygame.draw.rect(tela, cor_verde, [0,tela_y - 30,tela_x,30])
        #Atualiza a tela
        pygame.display.update()

    #Fecha a janela e finaliza o jogo
    pygame.quit()



jogo_loop()
