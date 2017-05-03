#Head Soccer Game - Vitor, Gabriel, Pedro e Manzanna
#Programa main que rodará tudo

import pygame

def main():
    pygame.init()
    bg = pygame.image.load('background2.jpeg')
    tela = pygame.display.set_mode([876, 573])
    pygame.display.set_caption('Head Soccer Game')

    relogio = pygame.time.Clock()
    cor_verde = (0,128,0)

    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False



        #30 FPS
        relogio.tick(25)
        #Tela
        tela.fill(cor_verde)
        tela.blit(bg,(0,0,300,300))
        #Atualiza a tela
        pygame.display.update()



    #Fecha a janela e finaliza o jogo
    pygame.quit()



main()
