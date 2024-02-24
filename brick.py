import pygame

pygame.init() #initialize pygame

# window
SCREEN_WIDTH = 800 #pixel width
SCREEN_HEIGHT = 600 #pixel height

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #create the screen

# create a rectangle that can move around
player = pygame.Rect((300,250, 50, 50)) #xcor, ycor, xwidth, yheight

#loop the game window
run = True
while run:

    pygame.draw.rect(screen, (255,0, 0), player) #screen name, rgb, rectangle name
    
    #event handler, looks for events like mouse clicks and keyboard presses
    for event in pygame.event.get(): #iterate through all events picked up by pygame
        #closing the game window
        if event.type == pygame.QUIT:
            run = False;

    pygame.display.update() # continuously refreshes the screen

pygame.quit()