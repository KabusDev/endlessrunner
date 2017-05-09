import pygame
import sys
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
        self.pos_x = 0
        self.pos_y = 0

    def gravity_check(self):
        # gravity effect
        if self.pos_y == 0:
            self.pos_y = 1
        else:
            self.pos_y = 0.40

        # ground check
        if self.rect.y >= ui.res_y - self.rect.height and self.pos_y >= 0:
            self.pos_y = 0
            self.rect.y = ui.res_y - self.rect.height

    def jump(self):
        self.rect.y += 2
        self.rect.y -= 2
        if self.rect.bottom >= ui.res_y:
            self.pos_y = -10

    def update(self):
        self.gravity_check()
        self.rect.y += self.pos_y



def Controls():
    player = Player()
    for event in pygame.event.get():
        pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
                print("player jump")
                # todo write jumping for sprite

            if event.key == pygame.K_ESCAPE:
                print("pause menu")
                # todo write pause
        if event.type == pygame.QUIT:
            sys.exit()

def Logic():
    player = Player()
    player.rect.x = 340
    player.rect.y = ui.res_y - player.rect.height
    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(player)
    active_sprite_list.update()
    active_sprite_list.draw(ui.screen)

