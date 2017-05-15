import pygame
import ui
import game
import controls

pygame.init()
clock = pygame.time.Clock()
fps_counter = clock.get_fps()


pygame.display.set_caption('Endless Runner')


def update(dt):
    game.logic()
    controls.controls()
    pass

# main loop
while True:
    dt = clock.tick(60) / 1000
    # print(fps_counter)
    # todo use fps counter, debug commands?
    update(dt)

    ui.screen.fill(ui.RGB.white)  # redundant fill just incase ui doesnt change background fill of screen colour
    ui.render(ui.screen)

    pygame.display.flip()
