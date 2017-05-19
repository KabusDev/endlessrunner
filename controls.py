import pygame
import ui
import game
import sys

player = game.Player


def controls():
    for event in pygame.event.get():
        pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if ui.menu_check is False and ui.pause_check is False:
                    ui.ply.jump()
                pass

            if event.key == pygame.K_ESCAPE:
                if ui.menu_check is True:  # quick way of quitting the game? might remove
                    sys.exit()

                if ui.menu_check is False:  # stops pause from drawing on main menu
                    if ui.pause_check is False:
                        ui.pause_check = True
                        # have a method of pausing in-game loop but not main loop?
                    else:
                        ui.pause_check = False  # exit pause menu method
                    pass
                else:
                    pass

            if event.key == pygame.K_p:
                if ui.fps_check is False:
                    ui.fps_check = True
                    print("fps count enabled")
                else:
                    ui.fps_check = False
                    print("fps count disabled")

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            click = event.button
            if click == 1:
                if ui.menu_check is True:
                    if ui.play_button.collidepoint(mouse_pos):  # pycharm whining, still functions correctly
                        ui.ui_start_game()
                        print("start")
                    if ui.quit_button.collidepoint(mouse_pos):
                        sys.exit()
                if ui.pause_check is True:
                    if ui.continue_button.collidepoint(mouse_pos):
                        ui.pause_check = False
                    if ui.menu_button.collidepoint(mouse_pos):
                        print("test")
                        ui.menu_check = True
                        ui.pause_check = False
                else:
                    pass
        if event.type == pygame.QUIT:
            sys.exit()