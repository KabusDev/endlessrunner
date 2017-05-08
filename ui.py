import pygame

class ScrRes:
    def __init__(self,x,y):
        self.x = x
        self.y = y

svga = ScrRes(800, 600)
xga = ScrRes(1024, 768)
hdready = ScrRes(1280, 720)
sxga = ScrRes(1280, 1024)

# players wont see the var names, only the units for the rex
# hopefully going to have a menu where players can change settings, customised skeleton?
# using this style of class so that i can get seperate ints for modification

resolution = (svga.x, svga.y) # this will change in settings

# have checks for certain scales on existing assets and change them;
# to higher res assets if certain resolutions make them look low quality?


screen = pygame.display.set_mode(resolution)

class RGB:  # class for colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue  = (0, 0, 255)
    red   = (255, 0, 0)

game_event = True

class GameScreen():
    pass

def render(screen):
    if game_event is True:
        pygame.draw.rect(screen, RGB.blue, (0, 0, 20, 20))
        PlyObj = pygame.draw.circle(screen, RGB.blue, [40,250], 20)
    if game_event is False:
        pygame.draw.rect(screen, RGB.black, (0,0,40,40))
    pass


