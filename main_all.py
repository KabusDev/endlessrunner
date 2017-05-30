import pygame
import sys
# import time

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Endless Runner')

# variables & other stuff
pygame.font.init()
menu_check = True
pause_check = False
fps_check = False


class ScrRes:
    def __init__(self, x, y):
        self.x = x
        self.y = y

svga = ScrRes(800, 600)
xga = ScrRes(1024, 768)
hdready = ScrRes(1280, 720)
sxga = ScrRes(1280, 1024)

res_x = svga.x
res_y = svga.y
res_var = (res_x, res_y)

scale_var = (res_x * res_y / 10000)/2
res_scale = round(scale_var)
print(res_scale)  # hack way of getting scaling for text?

resolution = res_var  # this will change in settings
screen = pygame.display.set_mode(resolution, pygame.HWSURFACE)
# wont be used but might as well leave it here since it would take a while to change stuff back to res co-ords


class RGB:  # class for colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    black_alpha = (0, 0, 0, 65)
    grey = (178, 178, 178)

Font_Basic = pygame.font.SysFont("Calibri", 45, False, False)


class Rect:
    def __init__(self, surface, color, xy_loc):
        self.surface = surface
        self.color = color
        self.xy_loc = xy_loc

# make all rectangles scale to res
# i could use some vars from here for other applications eg text alignment.
scr_button_1 = Rect(screen, RGB.blue, (res_x/4, res_y/8, res_x/2, res_y/5))
scr_button_2 = Rect(screen, RGB.black, (res_x/4, res_y/1.5, res_x/2, res_y/5))
scr_overlay = Rect(screen, RGB.black_alpha, (0, 0, res_x, res_y))
level_box = Rect(screen, RGB.black, (0, res_y/1.25, res_x, res_y))


def collision_detect(self, sprite):
    return self.rect.colliderect(sprite.rect)


class Player():
    is_jumping = False
    # self.loc_x = round(res_x / 7)
    # self.loc_y = round(res_y / 1.31)
    loc_x = 100
    loc_y = 450
    force = 8
    mass = 2

    def jump(self):
        print("ply jump")  # debug
        self.is_jumping = True  # jump trigger

    def logic_update(self):
        # global f
        # time.sleep(0.5) # debug timer for prints

        # force calculation 0.5 * mass * velocity^2.
        if self.is_jumping is True:
            if self.force >= 0:
                f = -(0.5 * self.mass * (self.force * self.force))
            else:
                f = (0.5 * self.mass * (self.force * self.force))
            self.loc_y += f
            self.force -= 1

            if self.loc_y >= 450:
                self.loc_y = 450
                self.is_jumping = False
                self.force = 8

            # print(f)
            # print("force ", self.force)
            # print("loc ", self.loc_y)


class WorldGen:

    # todo del from file
    # shifting the world
    # use predefined obstacle patterns and apply patterns procedurally?
    # todo need function for detecting collisions between ply and obstacles
    # todo game over screen
    # todo pause state so that game only runs after starting to play

    def __init__(self):
        self.obstacle_group = pygame.sprite.Group()
        self.powerup_group = pygame.sprite.Group()  # low priority
        self.world_shift = 0  # use this to move the world instead of blocks independently?
        self.x_1 = 400
        self.x_2 = 700
        self.x_3 = 1100
        self.speed_var = 10 # this will be used to change acceleration speed of obstacles

    def obstacle_obj(self):

        triangle = pygame.draw.polygon(screen, RGB.blue,
                                      (((self.x_1-50), res_y / 1.25),
                                       (self.x_1, res_y / 1.5),
                                       ((self.x_1+50), res_y / 1.25)))

        triangle2 = pygame.draw.polygon(screen, RGB.blue,
                                        (((self.x_2 - 50), res_y / 1.25),
                                         (self.x_2, res_y / 1.5),
                                         ((self.x_2 + 50), res_y / 1.25)))

        triangle3 = pygame.draw.polygon(screen, RGB.blue,
                                        (((self.x_3 - 50), res_y / 1.25),
                                         (self.x_3, res_y / 1.5),
                                         ((self.x_3 + 50), res_y / 1.25)))



    # def world_shifter(self, shift_x):  # func for global shift in items, player is exempt
    #     self.world_shift += shift_x  # global shifting, something
    #
    #     for obstacle in self.obstacle_group:
    #         obstacle.rect.x += shift_x

        # todo powerup stuff later
        pass

    def world_update(self):
        # print (self.x_1)

        self.x_1 -= self.speed_var
        self.x_2 -= self.speed_var
        self.x_3 -= self.speed_var

        if self.x_1*1.2 <= -250:
            self.x_1 = 850
        if self.x_2*1.2 <= -250:
            self.x_2 = 850
        if self.x_3*1.2 <= -250:
            self.x_3 = 850
        pass
    pass


class Obstacles():
    # do polygons that change on x axis for horizontal movement to simulate level progression?
    # y should be static, x should be dynamically changed, use modifier from one int var?

    # x as centre, (x*.5,res_y/1.25), (x,res_y/1.5), (x*1.5,res_y/1.25) ?
    # x would have to have about 50~ pixels in between?, should be equilateral
    # something like this for placements of obstacles
    pass


ply = Player()
world = WorldGen()


def main_menu():
    global play_button, quit_button

    play_button = pygame.draw.rect(scr_button_1.surface, scr_button_1.color, scr_button_1.xy_loc)
    quit_button = pygame.draw.rect(scr_button_2.surface, scr_button_2.color, scr_button_2.xy_loc)

    play_txt = Font_Basic.render("Play", 1, RGB.white, None)
    quit_txt = Font_Basic.render("Quit", 1, RGB.red, None)

    screen.blit(play_txt, (res_x / 2.25, res_y / 5.5))
    screen.blit(quit_txt, (res_x / 2.25, res_y / 1.375))

    pass


def pause_menu():
    global continue_button, menu_button

    background_menu = pygame.draw.rect(scr_overlay.surface, scr_overlay.color, scr_overlay.xy_loc)
    continue_button = pygame.draw.rect(scr_button_1.surface, scr_button_1.color, scr_button_1.xy_loc)
    menu_button = pygame.draw.rect(scr_button_2.surface, scr_button_1.color, scr_button_2.xy_loc)

    continue_txt = Font_Basic.render("Resume", 1, RGB.white, None)
    menu_txt = Font_Basic.render("Quit to Menu", 1, RGB.red, None)

    screen.blit(continue_txt, (res_x / 2.5, res_y / 5.5))
    screen.blit(menu_txt, (res_x / 2.8, res_y / 1.375))
    pass


def game_screen():
    player_ball = pygame.draw.circle(screen, RGB.black, (round(ply.loc_x), round(ply.loc_y)), 30)
    bounds = pygame.draw.rect(level_box.surface, level_box.color, level_box.xy_loc)  # constant
    world.obstacle_obj()
    pass


def controls():
    for event in pygame.event.get():
        pygame.key.get_pressed()
        global menu_check, pause_check

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if menu_check is False and pause_check is False:
                    ply.jump()
                pass

            if event.key == pygame.K_ESCAPE:
                if menu_check is True:  # quick way of quitting the game? might remove
                    sys.exit()

                if menu_check is False:  # stops pause from drawing on main menu
                    if pause_check is False:
                        pause_check = True
                        # have a method of pausing in-game loop but not main loop?
                    else:
                        pause_check = False  # exit pause menu method
                    pass
                else:
                    pass

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            click = event.button
            if click == 1:
                if menu_check is True:
                    if play_button.collidepoint(mouse_pos):  # pycharm whining, still functions correctly
                        ui_start_game()
                        print("start")
                    if quit_button.collidepoint(mouse_pos):
                        sys.exit()
                if pause_check is True:
                    if continue_button.collidepoint(mouse_pos):
                        pause_check = False
                    if menu_button.collidepoint(mouse_pos):
                        print("test")
                        menu_check = True
                        pause_check = False
                else:
                    pass
        if event.type == pygame.QUIT:
            sys.exit()


def render_logic():
    if menu_check is True:
        # main menu
        main_menu()

    if menu_check is False:
        game_screen()

    if pause_check is True:
        pause_menu()


def render(screen):
    # if fps_check is True:
    #     fps()
    render_logic()
    pygame.display.flip()


def ui_start_game():
    global menu_check
    if menu_check is True:
        menu_check = False
    pass


def update():
    world.world_update()
    ply.logic_update()
    controls()
    render(screen)
    pass


# main loop, may need changing for pause menu ect
while True:
    pygame.event.pump()
    dt = clock.tick(60) / 1000
    fps_counter = clock.get_fps()
    # print(fps_counter)
    update()
    screen.fill(RGB.white)  # redundant fill just in case ui doesnt change background fill of screen colour
