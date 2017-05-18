import pygame
# import game

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

# players wont see the var names, only the units for the res
# hopefully going to have a menu where players can change settings, customised skeleton?
# using this style of class so that i can get seperate ints for modification
# probably too much work

res_x = svga.x
res_y = svga.y
res_var = (res_x, res_y)

basic_scale_var = (res_x * res_y / 10000)
# print(basic_scale_var) # hack way of getting scaling for text?

resolution = res_var  # this will change in settings

# have checks for certain scales on existing assets and change them;
# to higher res assets if certain resolutions make them look low quality?

screen = pygame.display.set_mode(resolution)


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
    pygame.draw.rect(screen, RGB.blue, (0, 0, 20, 20))  # debug box
    bounds = pygame.draw.rect(level_box.surface, level_box.color, level_box.xy_loc)
    pass


def fps(self):
    pass


def render(screen):
    # if fps_check is True:
    #     fps()
    if menu_check is True:
        # main menu
        main_menu()

    if menu_check is False:
        game_screen()
        # this is how i will switch from a menu to the game
        # menu doesnt have to be implemented, more of a test of capabilities than a specification

    if pause_check is True:
        pause_menu()
    pass


def ui_start_game():
    global menu_check
    if menu_check is True:
        menu_check = False
    pass
