import pygame
from os import path

pygame.init()

WIDTH = 852
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH,HEIGHT))


game_folder = path.dirname(__file__) #pasta do jogo
img_folder = path.join(game_folder, "Imagens") #pasta de imagens
titulo = pygame.image.load(path.join(img_folder, "titulo.PNG")).convert() #imagem do titulo
#titulo1 = titulo.get_rect()
#titulo1.rect.x = WIDTH/2
bright_play = pygame.image.load(path.join(img_folder, "bright_play.PNG")).convert() # botão play com o mouse em cima
play = pygame.image.load(path.join(img_folder, "play.PNG")).convert() #botão play
quit = pygame.image.load(path.join(img_folder, "quit.PNG")).convert() #botão quit
quit_bright = pygame.image.load(path.join(img_folder, "quit_bright.PNG")).convert() #botão quit com o mouse em cima
background1 = pygame.image.load(path.join(img_folder, "background1.JPG")).convert() #fundo
background2 = background1.get_rect()
screen.blit(background1, background2)

# função menu
def menu():
	intro = True
	while intro:
		
		screen.blit (titulo, (WIDTH*1/7,0))
		button(play,128,360,298,426,bright_play,action = "play")
		button(quit,561,360,717,435,quit_bright,action = "quit")

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			#print (event)
			#if event.type == pygame.MOUSEBUTTONDOWN:

		pygame.display.update()

#função dos botões
def button(img, x, y, width, height, img1, action = None):
	global paused
	global tela
	cur = pygame.mouse.get_pos()
	click =pygame.mouse.get_pressed()
	screen.blit (img, (x,y))
	if x+width > cur[0] > x and y+height > cur[1] > y:
		screen.blit(img, (x,y))
		if click[0] == 1 and action != None:
	
			#se der tempo/ nao tiver funcionando colocar na função menu

			if action == "play":
				Game()
				
	
			elif action == "quit":
				pygame.quit()
				quit()

			elif action == "menu":
				screen
				menu()
	else:
		screen.blit(img1, (x,y))

#fazer um game loop


menu()