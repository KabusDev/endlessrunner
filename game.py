import pygame, sys
import ui



def Controls():
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()

        # if ui.test is True:
        if event.type == pygame.KEYDOWN:
            if pressed[pygame.K_KP_ENTER]:
                ui.game_event = True

            if pressed[pygame.K_a]:
                ui.game_event = False

        if event.type == pygame.QUIT:
            sys.exit()