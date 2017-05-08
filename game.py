import pygame, sys
import objects



def Controls():
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()

        # if ui.test is True:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("player jump")
                # todo write jumping for sprite

        if event.type == pygame.QUIT:
            sys.exit()