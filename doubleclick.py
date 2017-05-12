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
timer2 = 0
dt = 0.1

while exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = False
		if event.type == pygame.KEYDOWN:
			if event.key == seta_direita:		
				print("Moveu Direita")
				if timer == 0:  # First click.
				 	timer = 0.001 # Start the timer.
				 	print("s")
				if timer != 0 :
					print("k")
					timer += dt
					pygame.time.delay(100)
				#Click again before 0.3 seconds to double click.
				elif timer < 0.3:
					print('Dash Direita')
					timer = 0					
				# Increase timer after mouse was pressed the first time.
				
				# Reset after 0.3 seconds.
				elif timer >= 0.3:
					timer = 0
			elif event.key == seta_esquerda:
				print("Moveu Esquerda")
				if timer2 == 0:  # First click.
				 	timer2 = 0.001 # Start the timer.
				#Click again before 0.3 seconds to double click.
				if timer2 < 0.3:
					print('Dash Esquerda')
					timer2 = 0
				# Increase timer after mouse was pressed the first time.
				if timer2 != 0:
					timer2 += dt
					pygame.time.delay(100)
				# Reset after 0.3 seconds.
				if timer2 >= 0.3:
					timer2 = 0
		
pygame.display.update()
pygame.quit()
quit()