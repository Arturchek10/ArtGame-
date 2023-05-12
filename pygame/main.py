import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((640, 360)) #flags=pygame.NOFRAME без рамки    ->  это размеры окна игры
pygame.display.set_caption('Proger Game')  #-> название окна / игры   
icon = pygame.image.load('images/icon.png') # иконка игры 
pygame.display.set_icon(icon) 

#screen.fill((128, 61, 179)) окрашивание экрана 

myfont = pygame.font.Font('fonts/DarumadropOne-Regular.ttf', 40)  # шрифт 
text_surface = myfont.render('ArtGGGame' , True , (175, 95, 220))   #шрифт

label = pygame.font.Font('fonts/DarumadropOne-Regular.ttf', 40) 
lose_label = myfont.render('you lose', False, (0, 0, 0))
restart_label = label.render('restart', False, (240, 11, 11))
restart_label_rect = restart_label.get_rect(topleft=(260, 280))

walk_right = [pygame.image.load('images/playerRight/player1.png').convert_alpha(), pygame.image.load('images/playerRight/player2.png').convert_alpha(), pygame.image.load('images/playerRight/player3.png').convert_alpha(), pygame.image.load('images/playerRight/player4.png').convert_alpha(), pygame.image.load('images/playerRight/player5.png'), pygame.image.load('images/playerRight/player6.png').convert_alpha(), pygame.image.load('images/playerRight/player7.png').convert_alpha(), pygame.image.load('images/playerRight/player8.png').convert_alpha(),] 


bg = pygame.image.load ('images/bg.jpg').convert_alpha()

player_anim_count = 0
enemy_anim_count = 0 

bg_x = 0 
over = pygame.image.load ('images/game-over-screen.jpg')
bg_sound = pygame.mixer.Sound ('audio/fon_music.mp3')
bg_sound.play()
 
lose_sound = pygame.mixer.Sound ('audio/lose_sound.wav')

player_speed_up = 6
player_speed_down = 12
player_x = 50
player_y = 247
jump = False
jump_count = 7 
ghost_x = 250
ghost = pygame.image.load('images/ghost.png').convert_alpha()

gameplay = True 

running = True

while running:

	screen.blit(bg, (bg_x, 0))
	screen.blit(bg, (bg_x + 640, 0))

	if gameplay:
		screen.blit(text_surface, (230, 50))
		screen.blit(walk_right[player_anim_count], (player_x, player_y))
		screen.blit(ghost, (ghost_x, 255))

		#отслеживание соприкосновений
		player_rect = walk_right[0].get_rect(topleft=(player_x, player_y))
		ghost_rect = ghost.get_rect(topleft=(ghost_x, 240))
		
		if player_rect.colliderect(ghost_rect):
			gameplay = False 

		#движение вправо влево
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT] and player_x < 550:
			player_x += player_speed_up
		elif keys[pygame.K_LEFT] and player_x > 10:
			player_x -= player_speed_down
		
		#прыжок 
		if not jump:
			if keys[pygame.K_SPACE]:
				jump = True
		else:
			if jump_count >= -7:
				if jump_count > 0: 
					player_y -= (jump_count ** 2) / 2
				else:
					player_y += (jump_count ** 2) / 2
				jump_count -= 1 
			else: 
				jump = False 
				jump_count = 7		 
		
		#анимация движения героя (кадровка сплитов)
		if player_anim_count == 7:
			player_anim_count = 0
		else:
			player_anim_count += 1 

		# смещение двух задних фонов 
		bg_x -= 2
		if bg_x == -640:
			bg_x = 0 

		ghost_x -= 3
		if ghost_x <= -10:
			ghost_x = 660 


		player_x += 3
		if player_x >= 570:
			player_x = 570

	else: 
		screen.blit(over, (-50, -50))
		bg_sound.stop()
		screen.blit(restart_label, restart_label_rect)

	pygame.display.update()	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
					
	
	clock.tick(11)
			 
							
