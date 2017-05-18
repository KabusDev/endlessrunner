import pygame
import ui

is_jumping = False


class Player:
    def __init__(self):
        ply_width = 50  # these will scale with the game res
        ply_height = 50
        self.image = pygame.Surface((ply_width, ply_height))
        self.image.fill(ui.RGB.blue)

        # world location of player, should be static on x axis but changes on y axis
        self.loc_x = 0
        self.loc_y = 0

        self.force = 8
        self.mass = 2


def jump():
    global is_jumping
    print("a")  # debug
    if is_jumping is False:  # should stop multiple jumps while jumping
        is_jumping = True  # jump trigger


def logic_update(self):
    # force calculation 0.5 * mass * velocity^2.
    if self.is_jumping:
        if self.force > 0:
            f = (0.5 * self.mass * (self.force * self.force))
        else:
            f = -(0.5 * self.mass * (self.force * self.force))

        self.loc_y = self.loc_y - f
        self.force = self.force - 1

        if self.loc_y >= 0:
            self.y = 0
            self.is_jumping = False
            self.force = 8


def logic():

    # todo rewrite all playable functionality
    pass

