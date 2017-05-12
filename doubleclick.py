import pygame

pygame.init()


display = pygame.display.set_mode((800,600))
exit = True

seta_cima = 273
seta_baixo = 274
seta_direita = 275
seta_esquerda = 276

clock = pygame.time.Clock()
dt = 0.1

while exit:
	for event in pygame.event.get():
		timer = 0
		if event.type == pygame.QUIT:
			exit = False
		if event.type == pygame.KEYDOWN:
				if event.key == seta_direita:		
					print("Moveu Direita")
					timer = 0.001
		while timer < 0.2:
			if event.type == pygame.KEYDOWN:
				if event.key == seta_direita:		
					print("dash")
					timer += dt

	pygame.display.update()
pygame.quit()
quit()