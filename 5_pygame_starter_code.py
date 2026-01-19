

import pygame

pygame.init()

screen = pygame.display.set_mode((1200,700))

pygame.display.set_caption("kmeans visualization")

running = True

clock = pygame.time.Clock()

BACKGROUND = (214, 214, 214)

while running:
	clock.tick(60)
	screen.fill(BACKGROUND)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()

pygame.quit()