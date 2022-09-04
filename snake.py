import pygame
import random
import time

speed = 25

w_x = 1000
w_y = 800

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

pygame.init()

pygame.display.set_caption('worm')
window = pygame.display.set_mode((w_x, w_y))

fps = pygame.time.Clock()

snake_pos = [100, 50]

body = [[100, 50], [90, 50], [70, 50], [60, 50], [50, 50], [40, 50]]

fruit_pos = [random.randrange(1, (w_x//10)) * 10, random.randrange(1, (w_y//10)) * 10]
fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0 

def Score(choice, color, font, size):
	
	score_font = pygame.font.SysFont(font, size)
	score_surface = score_font.render('Score: ' + str(score), True, color)
	score_rect = score_surface.get_rect()

	window.blit(score_surface, score_rect)

def game_over():
	
	window.fill(black)

	over_font = pygame.font.SysFont('times new roman', 50)
	over_surface = over_font.render('Your Score is: ' + str(score), True, red)
	over_rect = over_surface.get_rect()	
	over_rect.midtop = (w_x/2, w_y/4)

	window.blit(over_surface, over_rect)

	pygame.display.flip()

	time.sleep(4)
	pygame.quit()
	quit()

while True:

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				quit()


	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	if direction == 'UP':
		snake_pos[1] -= 10
	if direction == 'DOWN':
		snake_pos[1] += 10
	if direction == 'LEFT':
		snake_pos[0] -= 10
	if direction == 'RIGHT':
		snake_pos[0] += 10
	
	body.insert(0, list(snake_pos))

	if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
		score += 10
		fruit_spawn = False
	else:
		body.pop()
	
	if fruit_spawn == False:
		fruit_pos = [random.randrange(1, (w_x//10)) * 10, random.randrange(1, (w_y//10)) * 10]
	
	fruit_spawn = True
	window.fill(black)

	for pos in body:
		pygame.draw.rect(window, green, pygame.Rect(
          pos[0], pos[1], 10, 10))
	
	pygame.draw.rect(window, red, pygame.Rect(
      fruit_pos[0], fruit_pos[1], 10, 10))

	if snake_pos[0] < 0 or snake_pos[0] > w_x-10:
		game_over()
	if snake_pos[1] < 0 or snake_pos[1] > w_y-10:
		game_over()

	for snek in body[1:]:
		if snake_pos[0] == snek[0] and snake_pos[1] == snek[1]:
			game_over()

	Score(1, white, 'times new roman', 40)

	pygame.display.update()
	fps.tick(speed)