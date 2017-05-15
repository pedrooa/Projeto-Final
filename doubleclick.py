import pygame

pygame.init()


display = pygame.display.set_mode((800,600))
exit = True

seta_cima = 273
seta_baixo = 274
seta_direita = 275
seta_esquerda = 276

global clock, double_click_event, timer
double_click_event = pygame.USEREVENT + 1
timer = 0


while exit:
	
	for event in pygame.event.get():
		timer = 0
		if event.type == pygame.QUIT:
			exit = False
		if event.type == pygame.K_RIGHT:
			if timer == 0:
				pygame.time.set_timer(double_click_event, 500)
				timerset = True
			else:
				if timer == 1:
					pygame.time.set_timer(double_click_event, 0)
					double_click()
					timerset = False
			if timerset:
				timer = 1
			else: 
				timer = 0
		elif event.type == double_click_event:
			# timer timed out
			pygame.time.set_timer(double_click_event, 0)
			timer = 0
			print("evt = dble click")

	pygame.display.update()
pygame.quit()
quit()