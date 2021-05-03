from pygame import display, font, event, quit, QUIT, MOUSEBUTTONDOWN
from sys import exit
from random import randint
from time import time, sleep

font.init()
screenw = 1200
screenh = 800
screen = display.set_mode((screenw, screenh))
colours = [(127, 230, 101), (255, 0, 0), (0, 0, 0)]
font1 = font.Font("comicsans.TTF", 100)
font2 = font.Font("comicsans.TTF", 80)

def dotest(event):
	times = 5
	scores = []
	while True and times > 0:
		screen.fill(colours[0])
		display.update()
		timer = (randint(2000, 8000))/1000
		sleep(timer)
		event.clear(eventtype=MOUSEBUTTONDOWN)
		screen.fill(colours[1])
		display.update()
		unclicked = True
		start_time = time()
		while unclicked == True:
			for e in event.get():
				if e.type == MOUSEBUTTONDOWN:
					unclicked = False
					end_time = time()
				elif e.type == QUIT:
					quit()
					exit()
		times-=1
		timetaken = round((end_time-start_time), 3)
		text = font1.render((f"{str((int((timetaken*1000))))} millseconds"), 1,  colours[2])
		screen.blit(text, (350, 100))
		display.update()
		scores.append(timetaken)
		sleep(3)
	average = round((sum(scores)/len(scores)), 3)
	screen.fill(colours[0])
	text = font2.render((f"Average time taken was {str((int((average*1000))))} millseconds"), 1,  colours[2])
	screen.blit(text, (50, 100))
	display.update()
	sleep(5)


def start():
	while True:
		screen.fill(colours[0])
		text = font1.render("Click to Start", 1, colours[2])
		screen.blit(text, (350, 100))
		display.update()
		for e in event.get():
			if e.type == QUIT:
				quit()
				exit()
			elif e.type == MOUSEBUTTONDOWN:
				dotest(event)
start()