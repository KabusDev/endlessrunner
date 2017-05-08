import pygame, sys
import ui

class Player(pygame.sprite.Sprite):
    # pygame.sprite.Sprite is a class type for visible objects in pygame.
    def __init__(self):
        super().__init__()

        x = 50
        y = 50
        self.image = pygame.Surface([x, y])
        self.image.fill(ui.RGB.blue)

        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0

    pass

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