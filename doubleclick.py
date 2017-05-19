import pygame

pygame.init()


display = pygame.display.set_mode((800,600))
exit = True

seta_cima = 273
seta_baixo = 274
seta_direita = 275
seta_esquerda = 276

clock = pygame.time.Clock()
timer = 0
dt = 0

while exit:
	

	for event in pygame.event.get():
		timer = 0
		if event.type == pygame.QUIT:
			exit = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LSHIFT:
				#Velocidade do player duplica e depois de algum tempo volta ao normal
			if event.key == pygame.K_RCTRL:
				#Velocidade do player duplica e depois de algum tempo volta ao normal



	pygame.display.update()
pygame.quit()
quit()