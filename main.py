import pygame
import ui
import game
import controls

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption('Endless Runner')


def update():
    game.logic()
    controls.controls()
    pass


@ui.fps
def fps_func():
    fps = ui.Font_Basic.render(str(fps_counter), 1, ui.RGB.black, None)
    ui.render(ui.screen.blit(fps, (0, 0)))


# main loop, may need changing for pause menu ect
while True:
    dt = clock.tick(60) / 1000
    fps_counter = clock.get_fps()
    # print(fps_counter)
    update()
    ui.screen.fill(ui.RGB.white)  # redundant fill just incase ui doesnt change background fill of screen colour
    ui.render(ui.screen)

    pygame.display.flip()
