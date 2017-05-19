import pygame
import ui
import res

is_jumping = False


class Player():
    def __init__(self):
        super().__init__()
        self.ply_x = round(res.res_x / 7)
        self.ply_y = round(res.res_y / 1.31)

        # world location of player, should be static on x axis but changes on y axis
        self.loc_x = self.ply_x
        self.loc_y = self.ply_y

        self.force = 8
        self.mass = 2

    def player_appearance(self):
        global player_ball
        player_ball = pygame.draw.circle(res.screen, ui.RGB.black, (self.loc_x, self.loc_y), res.res_scale)
        pass


    def jump(self):
        global is_jumping
        print("ply jump")  # debug
        is_jumping = True  # jump trigger


    # def collision_detect(self, sprite):
    #     return self.rect.colliderect(sprite.rect)


    def logic_update(self):
        global is_jumping
        ply = ui.ply
        # force calculation 0.5 * mass * velocity^2.
        if is_jumping is True:
            if ply.force > 0:
                f = (0.5 * ply.mass * (ply.force * ply.force))
            else:
                f = -(0.5 * ply.mass * (ply.force * ply.force))
            ply.loc_y = ply.loc_y + f
            ply.force = ply.force - 1

            if ply.loc_y >= round(res.res_y / 1.31):
                ply.loc_y = round(res.res_y / 1.31)
                is_jumping = False
                ply.force = 8

def update():
    ply = Player()
    ply.logic_update()