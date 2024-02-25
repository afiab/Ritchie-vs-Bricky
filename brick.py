import pygame

pygame.init() #initialize pygame

# window
SCREEN_WIDTH = 800 # pixel width
SCREEN_HEIGHT = 600 # pixel height

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #create the screen

# create a rectangle that can move around
player = pygame.Rect((300,250, 50, 50)) #xcor, ycor, xwidth, yheight

#loop the game window
run = True
while run:

    screen.fill((0,0,0)) #refresh the screen by filling it black

    pygame.draw.rect(screen, (255,0, 0), player) #screen name, rgb, rectangle name
    
    key = pygame.key.get_pressed() # know what key has been pressed
    # arrow key movement
    if key[pygame.K_a]: # move left
        player.move_ip( -1, 0) #player moves in place -1 right (so left), and none up
    elif key[pygame.K_d]: # move right
        player.move_ip( 1, 0) #player moves in place 1 right and none up
    elif key[pygame.K_w]: # move up
        player.move_ip( 0, -1) #player moves in place none right and up 1
    elif key[pygame.K_s]: # move up
        player.move_ip( 0, 1) #player moves in place none right and up 1

    #event handler, looks for events like mouse clicks and keyboard presses
    for event in pygame.event.get(): #iterate through all events picked up by pygame
        #closing the game window
        if event.type == pygame.QUIT:
            run = False;

    pygame.display.update() # continuously refreshes the screen

pygame.quit()