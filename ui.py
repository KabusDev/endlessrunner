import pygame

class ScrRes:
    def __init__(self, x, y):
        self.x = x
        self.y = y

svga = ScrRes(800, 600)
xga = ScrRes(1024, 768)
hdready = ScrRes(1280, 720)
sxga = ScrRes(1280, 1024)

# players wont see the var names, only the units for the rex
# hopefully going to have a menu where players can change settings, customised skeleton?
# using this style of class so that i can get seperate ints for modification

res_x = sxga.x
res_y = sxga.y
res_var = (res_x, res_y)

resolution = res_var # this will change in settings

# have checks for certain scales on existing assets and change them;
# to higher res assets if certain resolutions make them look low quality?

screen = pygame.display.set_mode(resolution)

class RGB:  # class for colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    blackA = (0, 0, 0, 65)

menu_check = True

def collision(self, point):
    return self.rect.collision(point)

class Buttons():
    def __init__(self, surface, color, xy_loc):
        self.surface = surface
        self.color = color
        self.xy_loc = xy_loc
# make all rectangles scale to res
scr_button = Buttons(screen, RGB.black, (res_x/4, res_y/8, res_x/2, res_y/4))
scr_overlay = Buttons(screen, RGB.blackA, (0, 0, res_x, res_y))


def MainMenu():

    pass

def PauseMenu():
    pass

def GameScreen():
    # pygame.draw.rect(screen, RGB.blue, (0, 0, 20, 20)) # debug box
    pygame.draw.rect(scr_button.surface, scr_button.color, scr_button.xy_loc)

def render(screen):
    if menu_check is True:
        #main menu
        GameScreen()

    if menu_check is False:
        pygame.draw.rect(screen, RGB.black, (0, 0, 40, 40))
        # this is how i will switch from a menu to the game
        # menu doesnt have to be implemented, more of a test of capabilities than a specification

    pass

