import pygame
import os

# window
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 500 # pixel width, height
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #create the screen
pygame.display.set_caption("Ritchie vs Bricky") # set title of the window

WHITE = (255,255,255) # pass in rgb vals as a tuple

FPS = 60 # Frames per second

# sprites: Ritchie and Bricky
RITCHIE_IMAGE = pygame.image.load(os.path.join('Assets', 'ritchie.png')) # ritchie
RITCHIE_IMAGE = pygame.transform.scale(RITCHIE_IMAGE, (536/2.5,458/2.5)) #resize to size specified
BRICKY_IMAGE = pygame.image.load(os.path.join('Assets', 'bricky.png')) # bricky
BRICKY_IMAGE = pygame.transform.scale(BRICKY_IMAGE, (536/2.5,458/2.5)) #resize to size specified

def draw_window():
    #updates the window
    WIN.fill(WHITE) # fill the window with White
    WIN.blit(RITCHIE_IMAGE, (100,100)) # image, coords
    WIN.blit(BRICKY_IMAGE, (400,100)) # image, coords
    pygame.display.update() # continuously update the display

def main():
    clock = pygame.time.Clock() # to help do FPS
    run = True
    while run:
        clock.tick(FPS) # control the Frame Rate
        for event in pygame.event.get(): # loop through all the events
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main() # only run file directly