import random
import pygame
import pygame_helper
import math


def move(item, dt):
    """
    This function is designed to move an object in random motion
    :param item: library containing the "x", "y", "dx", "dy" key
    :param dt: the time taken for one iteration
    :return: new x and y coordinate for the object
    """
    n = random.randrange(5)

    # add dx to x to change position
    item["x"] = item["x"] + item["dx"] * dt
    item["y"] = item["y"] + item["dy"] * dt

    # random motion for the bee in the x direction
    if n == 1:
        item["dx"] = -item["dx"]

    # if we hit either side of the window reverse direction
    if item["x"] < 0:
        item["x"] = 0
        item["dx"] = -item["dx"]
    elif item["x"] + bee["w"] >= side:
        item["x"] = side - bee["img"].get_width()
        item["dx"] = -item["dx"]

    # if we hit the bottom or top change the direction
    if item["y"] < 0:
        item["y"] = 0
        item["dy"] = -item["dy"]

    elif item["y"] + bee["img"].get_height() >= side:
        item["y"] = side - bee["img"].get_height()
        item["dy"] = -item["dy"]

    return item


def distance(item1, item2):
    """
    compute the distance between 2 points
    :param item1: dict of item
    :param item2: dict of a second particle
    :return: the distance between the two coordinates
    """
    # item1["x"] += item1["img"].get_width() // 2
    # item1["y"] += item1["img"].get_height() // 2
    # item2["x"] += item2["img"].get_width() // 2
    # item2["y"] += item2["img"].get_height() // 2
    return math.sqrt((item2["x"] - item1["x"]) ** 2 + (item2["y"]-item1["y"]) ** 2)

# create the window


side = 600

win = pygame.display.set_mode((side, side))

win.fill((255, 255, 255))
# load images into pygame
# grass image dict
# "img" -> the image loaded into pygame
# "w" -> width of image
# "h" -> height of image
grass = {}
grass["img"] = pygame.image.load("grass.png").convert_alpha()
grass["w"] = grass["img"].get_width()
grass["h"] = grass["img"].get_height()

# load other useful images into pygame and store them into variables
sand = pygame.image.load("sand.png").convert_alpha()

flower = pygame.image.load("flower.png").convert_alpha()
# hive = pygame.image.load("hive.png").convert_alpha()

# bee dict
bee = {}
bee["img"] = pygame.image.load("bee.png")
bee["x"] = 0
bee["y"] = side - bee["img"].get_height()
bee["dx"] = side // 2
bee["dy"] = side // 4
bee["w"] = bee["img"].get_width()
bee["h"] = bee["img"].get_height()
win.blit(bee["img"], (bee["x"], bee["y"]))


# swatter dict
swatter = {}
swatter["img"] = pygame.image.load("swatter.png").convert_alpha()
swatter["x"] = side // 3 - swatter["img"].get_width()
swatter["y"] = side // 2 - swatter["img"].get_height() // 2
swatter["dx"] = 10
swatter["dy"] = 10
swatter["w"] = swatter["img"].get_width()
swatter["h"] = swatter["img"].get_height()

# repeat key down motion 20ms at a time
pygame.key.set_repeat(1, 20)

# click to start the game
pygame_helper.wait_for_click()

# clock object
clock = pygame.time.Clock()

# creating a list to store all grass images in grid
p = []
for row in range(side // 3, side - grass["w"], 2 * grass["w"]):
    for col in range(grass["w"], side - grass["h"], 2 * grass["w"]):
        # display grass images at x and y coordinates
        # dict for grass images in grid
        g = {}
        grass["x"] = row
        grass["y"] = col
        p.append(grass)

        win.blit(grass["img"], (grass["x"], grass["y"]))


pygame_helper.wait_for_click()
while True:
    time = clock.tick(40) / 1000
    win.fill((255, 255, 255))

    # move the bee in random motion
    bee = move(bee, time)
    win.blit(bee["img"], (bee["x"], bee["y"]))

    for i in p:
        win.blit(grass["img"], (grass["x"], grass["y"]))

    # load swatter image onto the screen
    win.blit(swatter["img"], (swatter["x"], swatter["y"]))

    for i in range(len(p)):
        # check collision between grass and bee
        if distance(bee, p[i]) <= (bee["w"] / 2 + grass["w"] / 2):
            bee["x"] = 0
            bee["y"] = side - bee["h"]
            grass["img"] = flower

    # swatter motion
    # moving the swatter up and down
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                swatter["y"] -= swatter["dy"]
            elif event.key == pygame.K_DOWN:
                swatter["y"] += swatter["dy"]
    # keep swatter within bounds of the window
    if swatter["y"] < 0:
        swatter["y"] = 0
    elif swatter["y"] >= side - swatter["h"]:
        swatter["y"] = side - swatter["h"]

    # what happens when the bee collides with a swatter
    # if the bee collides with the swatter return to starting position
    if distance(bee, swatter) <= (swatter["w"] / 2 + bee["w"] / 2):
        # delay restarting by 50ms
        # pygame.time.delay(50)
        bee["x"] = 0
        bee["y"] = side - bee["h"]
        g["img"] = sand
        win.blit(grass["img"], (grass["x"], grass["y"]))

    pygame.display.update()
# TODO change a grass patch into sand
# TODO locate grass that is neither sand nor flower
# TODO create counter so that when you lose the game exits

