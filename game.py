import pygame
import sys
import ui


def controls():
    for event in pygame.event.get():
        pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # player.jump()
                print("player jump")
                # todo write jumping for sprite
                pass

            if event.key == pygame.K_ESCAPE:
                print("pause menu")
                # todo write pause
                pass
        if event.type == pygame.QUIT:
            sys.exit()


def logic():
    pass

