import pygame
import ui
# import game
import sys

def click_detect():
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            click = event.button
            if click == 1:
                if ui.menu_check is True:
                    if ui.play_button.collidepoint(mouse_pos): # pycharm whining, still functions correctly
                        ui.ui_start_game()
                        print("start")
                else:
                    pass
    pass


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