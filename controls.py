import pygame
import ui
# import game
import sys


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
                if ui.menu_check is True:
                    sys.exit()
                if ui.menu_check is False:
                    if ui.pause_check is False:
                        ui.pause_check = True
                    else:
                        ui.pause_check = False
                    pass
                else:
                    pass

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
        if event.type == pygame.QUIT:
            sys.exit()