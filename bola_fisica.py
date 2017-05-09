import pygame
import random
import math

background_colour = (255,255,255)

(width, height) = (300, 200)

class Particle:
    def __init__(self, position, size):
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.speed = 0.01
        self.angle = math.pi / 2  #em graus
    def display(self):
	    pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed






screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial Da Bola')
screen.fill(background_colour)

#primeira particula
my_first_particle = Particle((150, 50), 15)
my_first_particle.display()


#fazendo particula aleatorias!
size = random.randint(10, 20)
x = random.randint(size, width - size)
y = random.randint(size, height - size)
my_random_particle = Particle((x, y), size)
my_random_particle.display()

number_of_particles = 10
my_particles = []

for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)


    particle = Particle((x, y), size)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi*2)


    my_particles.append(Particle((x, y), size))






my_random_particle.display()

pygame.display.flip()
running = True
clock = pygame.time.Clock()
while running:

	for event in pygame.event.get():

	    if event.type == pygame.QUIT:
		    running = False
    #screen.fill(background_colour)

	for particle in my_particles:
	    particle.move()
	    particle.display()

	clock.tick(60)
	pygame.display.flip
pygame.quit()
 	

