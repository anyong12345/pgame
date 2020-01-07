import pygame

pygame.init()
screen = pygame.display.set_mode((600, 500))
done = False
warna_bg = (240,24, 55)

pygame.display.set_caption ("Hallo APP")


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and \
	event.key == pygame.K_ESCAPE:
			done = True

	screen.fill(warna_bg)
	pygame.draw.line(screen, (0, 255, 0), (300, 100), (200, 300))
	pygame.draw.line(screen, (0, 255, 0), (300, 100), (400, 300))
	pygame.draw.line(screen, (0, 255, 0), (200,170), (400, 300))
	pygame.draw.line(screen, (0, 255, 0), (200,170), (400, 170))
	pygame.draw.line(screen, (0, 255, 0), (200,300), (400, 170))
	pygame.draw.line(screen, (0, 255, 0), (200, 400), (200, 350))
	pygame.draw.line(screen, (0, 255, 0), (210, 400), (210, 350))
	pygame.draw.line(screen, (0, 255, 0), (210, 350), (240, 350))
	pygame.draw.line(screen, (0, 255, 0), (240, 400), (240, 350))
	pygame.draw.line(screen, (0, 255, 0), (250, 400), (250, 350))
	pygame.draw.line(screen, (0, 255, 0), (280, 350), (250, 350))
	pygame.draw.line(screen, (0, 255, 0), (280, 370), (250, 370))
	pygame.draw.line(screen, (0, 255, 0), (290, 400), (290, 350))
	pygame.draw.line(screen, (0, 255, 0), (320, 350), (290, 350))
	pygame.draw.line(screen, (0, 255, 0), (320, 350), (320, 400))
	pygame.draw.line(screen, (0, 255, 0), (320, 400), (290, 400))



	pygame.display.flip()