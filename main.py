# Example file showing a basic pygame "game loop"
import copy
import pygame
from map import drawMap, boards
from pacman import Pacman

# pygame setup
pygame.init()
screen_width = 900
screen_height = 950
counter = 0
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
player = Pacman()
mapa = copy.deepcopy(boards)




while running:
    # poll for events

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.playerOri(event)

    # fill the screen with a color to wipe away anything from last frame
    if counter < 19:
        counter += 1
    else:
        counter = 0
    player.check_wall(mapa, screen_width,screen_height)
    player.move_player()
    
    screen.fill("black")
    drawMap(screen_width, screen_height, screen, mapa)
    player.draw_player(counter, screen)
    


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


