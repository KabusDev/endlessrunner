import pygame


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

scale_var = (res_x * res_y / 10000)/2
res_scale = round(scale_var)
print(res_scale) # hack way of getting scaling for text?

resolution = res_var  # this will change in settings

# have checks for certain scales on existing assets and change them;
# to higher res assets if certain resolutions make them look low quality?

screen = pygame.display.set_mode(resolution)
