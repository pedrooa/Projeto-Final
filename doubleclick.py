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
dt = 0.1

while exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = False
		if event.type == pygame.KEYDOWN:
			if event.key == seta_direita:		
				if timer == 0:  # First mouse click.
				 	timer = 0.001 # Start the timer.
				# Click again before 0.2 seconds to double click.
				elif 0.1 < timer < 0.3:
					print('Dash')
					timer = 0
	       		# Increase timer after mouse was pressed the first time.
				if timer != 0:
					timer += dt
		            # Reset after 0.5 seconds.
					if timer >= 0.3:
						print('Move Direita apenas')
						timer = 0

pygame.display.update()
pygame.quit()
quit()