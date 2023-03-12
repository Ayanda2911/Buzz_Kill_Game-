# Computer Science Final Project: buzz kill
import pygame
import pygame_helper
import random

# function to allow the bee to move in random motion


def move(item):
    """
    This function is designed to move the bee in a random motion
    :param item: a dict that has a "x", "y", "dx", and "dy" key
    :param dt: the time the particle is set to take to travel
    :return: new x and t coordinate
    """
    item["dx"] = random.randrange(1, 3)
    item["x"] += item["dx"]

    item["dy"] = random.randrange(1, 3)
    item["y"] += item["dx"]

    # did we height a side wall
    if item["x"] < 0:
        item["x"] = 0
        item["dx"] = -item["dx"]
    elif item["x"] + bee["img"].get_width() >= side:
        item["x"] = side - bee["img"]
        item["dx"] = -item["dx"]

    # did we hit a top/ bottom wall
    if item["y"] < 0:
        item["y"] = 0
        item["dy"] = -item["dy"]

    elif item["y"] + bee["img"].get_height() >= side:
        item["y"] = side - bee["img"].get_height()
        item["dy"] = -item["dy"]

    return (item["x"], item["y"])



side = 600

win = pygame.display.set_mode((side, side))

win.fill((255, 255, 255))

# dict for importing bee on the screen
bee = {}
bee["img"] = pygame.image.load("bee.png").convert_alpha()
# starting bee location
bee["x"] = 0
bee_x = 0
bee_y = side - bee["img"].get_height()
bee["y"] = side - bee["img"].get_height() # - hive.get_height()
win.blit(bee["img"], (bee["x"], bee["y"]))

# wait for click to start the game
pygame_helper. wait_for_click()
# make the bee move
while (0 <= bee_x < side) and (0 <= bee_y < side):
    # tuple decomposition
    bee = move(bee)

# TODO start working on swatter motion
# TODO refer to ping to see how to move the swatter up and down

# load images into pygame
grass = pygame.image.load("grass.jpg").convert_alpha()
swatter = pygame.image.load("swatter.png").convert_alpha()
sand = pygame.image.load("sand.png").convert_alpha()
flower = pygame.image.load("flower.jpg").convert_alpha()
hive = pygame.image.load("hive.png").convert_alpha()

# grass_width = grass.get_width()
# grass_height = grass.get_height()
# r = grass_width

#

# draw grass images, spread out uniformly
for row in range(side//3, side - grass.get_width(), 2 * r):
    for col in range(r, side - grass.get_height(), 2 * r):
        g = {}
        g["x"] = row
        g["y"] = col
        g["img"] = grass
        win.blit(g["img"], (g["x"], g["y"]))

# input the the swatter, bee, beehive
# win.blit(swatter, (side // 3 - swatter.get_height() // 2, side - swatter.get_height()))
# win.blit(hive, (0, side - hive.get_height()))


# move the bee using move function
# while in the bounds of the window
# user can exit program
pygame.display.update()
pygame_helper.wait_for_quit()
