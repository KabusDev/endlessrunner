import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Endless Runner')

# variables & other stuff
pygame.font.init()
menu_check = True
pause_check = False
ply_dead = False

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

resolution = res_var  # this will change in settings
screen = pygame.display.set_mode(resolution, pygame.HWSURFACE)
# wont be used but might as well leave it here since it would take a while to change stuff back to res co-ords


class RGB:  # class for colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)

    green = (105, 242, 92)
    yellow = (237, 242, 92)
    red = (242, 92, 92)

    black_alpha = (0, 0, 0, 65)  # alpha doesnt work on draw.rect
    grey = (178, 178, 178)

background = RGB.white

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


class Player:
    is_jumping = False
    loc_x = 100
    loc_y = 450
    force = 8
    mass = 2

    def jump(self):
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


class WorldGen:
    # shifting the world
    # use predefined obstacle patterns and apply patterns procedurally?

    def __init__(self):
        self.obstacle_group = pygame.sprite.Group()
        self.powerup_group = pygame.sprite.Group()  # low priority
        self.world_shift = 0  # use this to move the world instead of blocks independently?
        self.x_1 = 800
        self.x_2 = 1100
        self.x_3 = 1500  # initial spawns, off screen
        # these will get modified for procedural gen
        self.speed_var = 10  # this will be used to change acceleration speed of obstacles

    def obstacle_obj(self):
        global triangle, triangle2, triangle3, ply_dead

        triangle = pygame.draw.polygon(
            screen, RGB.blue,
            (((self.x_1-50), res_y / 1.25),
             (self.x_1, res_y / 1.5),
             ((self.x_1+50), res_y / 1.25))
        )

        triangle2 = pygame.draw.polygon(
            screen, RGB.blue,
            (((self.x_2 - 50), res_y / 1.25),
             (self.x_2, res_y / 1.5),
             ((self.x_2 + 50), res_y / 1.25))
        )

        triangle3 = pygame.draw.polygon(
            screen, RGB.blue,
            (((self.x_3 - 50), res_y / 1.25),
             (self.x_3, res_y / 1.5),
             ((self.x_3 + 50), res_y / 1.25))
        )

        if triangle.collidepoint(ply.loc_x, ply.loc_y):
            ply_dead = True
        if triangle2.collidepoint(ply.loc_x, ply.loc_y):
            ply_dead = True
        if triangle3.collidepoint(ply.loc_x, ply.loc_y):
            ply_dead = True
        pass

    # todo power up stuff later

    def world_update(self):
        self.x_1 -= self.speed_var
        self.x_2 -= self.speed_var
        self.x_3 -= self.speed_var

        end_x = -250
        start_x_1 = 850
        start_x_2 = 850  # was using seperate variables to change positions via procedural method, abandoned
        start_x_3 = 850

        if self.x_1*1.2 <= end_x:  # looping movement of obstacles
            self.x_1 = start_x_1
        if self.x_2*1.2 <= end_x:
            self.x_2 = start_x_2
        if self.x_3*1.2 <= end_x:
            self.x_3 = start_x_3

    def reset(self):  # reset func
        self.x_1 = 800
        self.x_2 = 1100
        self.x_3 = 1500
        pass
    pass


ply = Player()
world = WorldGen()


class Points:
    def __init__(self):
        self.point_tick = 0
        self.points = 0

    def collisions(self):
        collide_1 = pygame.draw.rect(screen, background, (world.x_1-60, 270, 120, 250))
        collide_2 = pygame.draw.rect(screen, background, (world.x_2 - 60, 270, 120, 250))
        collide_3 = pygame.draw.rect(screen, background, (world.x_3 - 60, 270, 120, 250))

        if collide_1.collidepoint(ply.loc_x, ply.loc_y):
            self.point_tick += 1
        if collide_2.collidepoint(ply.loc_x, ply.loc_y):
            self.point_tick += 1
        if collide_3.collidepoint(ply.loc_x, ply.loc_y):
            self.point_tick += 1

        if self.point_tick == 4:  # horrible
            # bad but necessary for single points per obstacle jump
            self.point_tick = 0
            self.points += 1

    def reset(self):
        self.points = 0
points = Points()


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

    background_menu = pygame.draw.rect(scr_overlay.surface, RGB.grey, scr_overlay.xy_loc)
    continue_button = pygame.draw.rect(scr_button_1.surface, RGB.green, scr_button_1.xy_loc)
    menu_button = pygame.draw.rect(scr_button_2.surface, RGB.red, scr_button_2.xy_loc)

    continue_txt = Font_Basic.render("Resume", 1, RGB.black, None)
    menu_txt = Font_Basic.render("Quit to Menu", 1, RGB.black, None)

    screen.blit(continue_txt, (res_x / 2.5, res_y / 5.5))
    screen.blit(menu_txt, (res_x / 2.8, res_y / 1.375))
    pass


def game_screen():
    points.collisions()
    player_ball = pygame.draw.circle(screen, RGB.black, (round(ply.loc_x), round(ply.loc_y)), 30)
    bounds = pygame.draw.rect(level_box.surface, level_box.color, level_box.xy_loc)  # constant
    # hp_bar = pygame.draw.rect(screen, RGB.green, )
    world.obstacle_obj()
    score = Font_Basic.render(str(points.points), 1, RGB.black, None)
    screen.blit(score, (0, 0))
    # screen.blit(points.collide_1, (world.x_1-60, 270))
    pass


def game_over():
    global reset_button, menu_button2
    background_menu = pygame.draw.rect(scr_overlay.surface, RGB.black, scr_overlay.xy_loc)
    reset_button = pygame.draw.rect(scr_button_1.surface, RGB.green, scr_button_1.xy_loc)
    menu_button2 = pygame.draw.rect(scr_button_2.surface, RGB.red, scr_button_2.xy_loc)

    reset_txt = Font_Basic.render("Retry", 1, RGB.black, None)
    menu_txt = Font_Basic.render("Quit to Menu", 1, RGB.black, None)

    screen.blit(reset_txt, (res_x / 2.3, res_y / 5.5))
    screen.blit(menu_txt, (res_x / 2.8, res_y / 1.375))
    # this is just a clone of the pause screen,
    pass


def controls():
    for event in pygame.event.get():
        pygame.key.get_pressed()
        global menu_check, pause_check, ply_dead

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if menu_check is False and pause_check is False:
                    print("ply jump")
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
                        global_reset()
                        ui_start_game()
                    if quit_button.collidepoint(mouse_pos):
                        sys.exit()
                if pause_check is True:
                    if continue_button.collidepoint(mouse_pos):
                        pause_check = False
                    if menu_button.collidepoint(mouse_pos):
                        menu_check = True
                        pause_check = False
                if ply_dead is True:
                    # cant put global reset here as points should show on game over screen.
                    if reset_button.collidepoint(mouse_pos):
                        global_reset()
                        ply_dead = False
                    if menu_button2.collidepoint(mouse_pos):
                        global_reset()
                        menu_check = True
                        ply_dead = False

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

    if ply_dead is True:
        game_over()


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


def game_pause():
    if pause_check is True:
        world.speed_var = 0
    if pause_check is False:
        world.speed_var = 10
        # will replace this
        # todo correct restart of speed when modified
        # todo freeze player jump when in pause
        pass


def global_reset():  # func for funcs, saves space on triggering resets, easy to add too ect
    world.reset()
    points.reset()


def update():
    world.world_update()
    ply.logic_update()
    controls()
    game_pause()
    render(screen)
    pass


# main loop, may need changing for pause menu ect
while True:
    pygame.event.pump()
    dt = clock.tick(60) / 1000
    update()
    screen.fill(background)  # redundant fill just in case ui doesnt change background fill of screen colour
