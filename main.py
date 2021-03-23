import pygame, sys, random, time

pygame.font.init()
screenw = 1200
screenh = 800
screen = pygame.display.set_mode((screenw, screenh))
colours = [(127, 230, 101), (255, 0, 0), (0, 0, 0)]
font = pygame.font.SysFont("comicsans", 100)
font2 = pygame.font.SysFont("comicsans", 80)

def dotest():
	times = 5
	scores = []
	while True and times > 0:
		screen.fill(colours[0])
		pygame.display.update()
		timer = (random.randint(2000, 8000))/1000
		time.sleep(timer)
		pygame.event.clear(eventtype=pygame.MOUSEBUTTONDOWN)
		screen.fill(colours[1])
		pygame.display.update()
		unclicked = True
		start_time = time.time()
		while unclicked == True:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					unclicked = False
					end_time = time.time()
				elif event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
		times-=1
		timetaken = round((end_time-start_time), 3)
		text = font.render((f"{str((int((timetaken*1000))))} millseconds"), 1,  colours[2])
		screen.blit(text, (350, 100))
		pygame.display.update()
		scores.append(timetaken)
		time.sleep(3)
	average = round((sum(scores)/len(scores)), 3)
	screen.fill(colours[0])
	text = font2.render((f"Average time taken was {str((int((average*1000))))} millseconds"), 1,  colours[2])
	screen.blit(text, (50, 100))
	pygame.display.update()
	time.sleep(5)



while True:
	screen.fill(colours[0])
	text = font.render("Click to Start", 1, colours[2])
	screen.blit(text, (350, 100))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			dotest()