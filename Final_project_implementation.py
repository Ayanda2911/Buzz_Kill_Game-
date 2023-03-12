# Computer Science Final Project "Buzz Kill"
# The program below generates a game called " Buzz Kill"
# where the aim is to keep the bee from pollinating grass patches
# and turning them into flowers
# If the user manages to swat the bee, a grass patch turns into dirt
# and cannot be pollinated
# if the bee collides with the with a grass patch, it successfully
# pollinates it and turn it into a flower
# If there are more than 3 patches that are pollinated, the user loses
# if there are more than 3  patches that are turned into sand, th user wins
# if there is a draw, the user doesn't win or lose


import pygame
import pygame_helper
import random


def move(item, dt):
    """
    This function is designed to move an object in random motion
    :param item: library containing the "x", "y", "dx", "dy" key
    :param dt: the time taken for one iteration
    :return: new x and y coordinate for the object
    """
    # pick a random number from 4 numbers
    n = random.randrange(5)

    # add dx to x to change position
    item["x"] = item["x"] + item["dx"] * dt
    item["y"] = item["y"] + item["dy"] * dt

    # if  n = 1 change the direction of velocity
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




pygame.init()

# dimensions for the pygame window
side = 600

# create pygame window
win = pygame.display.set_mode((side, side))

win.fill((255, 255, 255))

# the following dicts have the following parameters
# items refers to grass, bee and swatter  for the game
# "img" -> image
# "x" -> x coordinate
# "y" -> y - coordinate
# "dy" -> the vertical speed of the item
# "dx" -> the horizontal speed of the item
# "w" -> the width of the item
# "h" -> the height of the item

# bee dict
bee = {}
bee["img"] = pygame.image.load("bee.png")
bee["x"] = 0
bee["y"] = side - bee["img"].get_height()
bee["dx"] = side // 2
bee["dy"] = side // 5
bee["w"] = bee["img"].get_width()
bee["h"] = bee["img"].get_height()

# swatter dict
swatter = {}
swatter["img"] = pygame.image.load("swatter.png").convert_alpha()
swatter["x"] = side // 3 - swatter["img"].get_width()
swatter["y"] = side // 2 - swatter["img"].get_height() // 2
swatter["dx"] = 10
swatter["dy"] = 10
swatter["w"] = swatter["img"].get_width()
swatter["h"] = swatter["img"].get_height()

# grass dict
grass = {}
grass["img"] = pygame.image.load("grass.png").convert_alpha()
grass["w"] = grass["img"].get_width()
grass["h"] = grass["img"].get_height()

# line 95 - 135 specific grass images
# with their images, x and coordinates specified

# grass 1
grass1_img = grass["img"]
grass1_x = 2 * side // 3 - grass["w"] // 2
grass1_y = side // 5 - grass["h"] // 2

# grass 2
grass2_img = grass["img"]
grass2_x = side // 2 - grass["w"] // 2
grass2_y = 2 * side // 5 - grass["h"] // 2

# grass 3
grass3_img = grass["img"]
grass3_x = side // 2 + 2 * grass["w"]
grass3_y = 2 * side // 5 - grass["h"] // 2

# grass 4
grass4_img = grass["img"]
grass4_x = 2 * side // 3 - grass["w"] // 2
grass4_y = 3 * side // 5 - grass["h"] // 2

# grass 5
grass5_img = grass["img"]
grass5_x = side // 2 - grass["w"] // 2
grass5_y = 4 * side // 5 - grass["h"] // 2

# grass 6
grass6_img = grass["img"]
grass6_x = side // 2 + 2 * grass["w"]
grass6_y = 4 * side // 5 - grass["h"] // 2

# load sand image into pygame and assign it to sand variable
sand = pygame.image.load("sand.png").convert_alpha()

# load flower image into pygame and assign it to sand variable
flower = pygame.image.load("flower.png").convert_alpha()

# load hive image into pygame and assign it to hive variable
hive = pygame.image.load("hive.png").convert_alpha()

# pygame clock object
clock = pygame.time.Clock()

# repeat key down motion 20ms at a time
pygame.key.set_repeat(1, 20)

# click to start game
pygame_helper.wait_for_click()

# initialize counts for the number of times you swat(count) and the number
# of times the bee collides with a grass patch(g_count)
count = 0
g_count = 0

while True:
    # limit to 60 fps
    time = clock.tick(60) / 1000

    # fill window with white
    win.fill((255, 255, 255))

    # upload hive image into bottom left corner
    win.blit(hive, (0, side - hive.get_height()))

    # upload swatter to window surface
    win.blit(swatter["img"], (swatter["x"], swatter["y"]))

    # move the bee in random motion by using the move function
    bee = move(bee, time)

    # display bee on screen
    win.blit(bee["img"], (bee["x"], bee["y"]))

    # display grass images on screen
    win.blit(grass1_img, (grass1_x, grass1_y))
    win.blit(grass2_img, (grass2_x, grass2_y))
    win.blit(grass3_img, (grass3_x, grass3_y))
    win.blit(grass4_img, (grass4_x, grass4_y))
    win.blit(grass5_img, (grass5_x, grass5_y))
    win.blit(grass6_img, (grass6_x, grass6_y))

    # swatter motion
    # moving the swatter up and down
    for event in pygame.event.get():
        # check if a key has been pushed downwards
        if event.type == pygame.KEYDOWN:
            # if it is the upward key
            if event.key == pygame.K_UP:
                # move in the negative y direction
                swatter["y"] -= swatter["dy"]
            # if it is a downward key
            elif event.key == pygame.K_DOWN:
                # move in the positive y direction
                swatter["y"] += swatter["dy"]
    # keep swatter within bounds of the window
    # if the swatter collides with the upper bound of the window
    if swatter["y"] < 0:
        # limit swatter to window upper bound
        swatter["y"] = 0
    # if the swatter collides with lower bound
    elif swatter["y"] >= side - swatter["h"]:
        # limit swatter so that it doesn't go beyond the window
        swatter["y"] = side - swatter["h"]

    # what happens when the bee collides with a swatter
    # if the bee collides with the swatter return to starting position
    if (swatter["y"] - bee["h"] <= bee["y"] <= swatter["y"] + swatter["h"]) and \
            (swatter["x"] - bee["w"] <= bee["x"] <= swatter["x"] + swatter["w"] + bee["w"]):
        bee["x"] = 0
        bee["y"] = side - bee["h"]

    # lines 114 to 231
    # checks if it is a grass patch
    # if it is a grass patch, it changes to a sand image
        if grass1_img == grass["img"]:
            grass1_img = sand
            count += 1
        elif grass2_img == grass["img"]:
            grass2_img = sand
            count += 1
        elif grass3_img == grass["img"]:
            grass3_img = sand
            count += 1
        elif grass4_img == grass["img"]:
            grass4_img = sand
            count += 1
        elif grass5_img == grass["img"]:
            grass5_img = sand
            count += 1
        elif grass6_img == grass["img"]:
            grass6_img = sand
            count += 1

    if count == 4:
        pygame.time.delay(100)
        # print you lost on console
        print("You lost!")
        pygame.display.quit()

    # lines 244 to 290 checks collisions between different grass surfaces and bee
    # check if bee collides with grass surfaces
    # if the grass surface is of a grass image
    # then it changes to flower image
    # increments g_count by 1
    if (grass6_y - bee["h"] <= bee["y"] <= grass6_y + grass["w"]) and \
            (grass6_x - bee["w"] <= bee["x"] <= grass6_x + grass["w"] + bee["w"]):
        if grass6_img == grass["img"]:
            grass6_img = flower
            bee["x"] = 0
            bee["y"] = side - bee["h"]
            g_count += 1




    if (grass5_y - bee["h"] <= bee["y"] <= grass5_y + grass["w"]) and \
            (grass5_x - bee["w"] <= bee["x"] <= grass5_x + grass["w"] + bee["w"]):
        if grass6_img == grass["img"]:
            grass5_img = flower
            bee["x"] = 0
            bee["y"] = side - bee["h"]
            g_count += 1

    if (grass4_y - bee["h"] <= bee["y"] <= grass4_y + grass["w"]) and \
            (grass4_x - bee["w"] <= bee["x"] <= grass4_x + grass["w"] + bee["w"]):
        if grass4_img == grass["img"]:
            grass4_img = flower
            bee["x"] = 0
            bee["y"] = side - bee["h"]
            g_count += 1

    if (grass3_y - bee["h"] <= bee["y"] <= grass3_y + grass["w"]) and \
            (grass3_x - bee["w"] <= bee["x"] <= grass3_x + grass["w"] + bee["w"]):
        if grass3_img == grass["img"]:
            grass3_img = flower
            bee["x"] = 0
            bee["y"] = side - bee["h"]
            g_count += 1

    if (grass2_y - bee["h"] <= bee["y"] <= grass2_y + grass["w"]) and \
            (grass2_x - bee["w"] <= bee["x"] <= grass2_x + grass["w"] + bee["w"]):
        if grass2_img == grass["img"]:
            grass2_img = flower
            bee["x"] = 0
            bee["y"] = side - bee["h"]
            g_count += 1

    if (grass1_y - bee["h"] <= bee["y"] <= grass1_y + grass["w"]) and \
            (grass1_x - bee["w"] <= bee["x"] <= grass1_x + grass["w"] + bee["w"]):
        if grass1_img == grass["img"]:
            grass1_img = flower
            bee["x"] = 0
            bee["y"] = side - bee["h"]
            g_count += 1

    # if the number of times the you swat is greater than half the the grass patches
    if g_count == 4:
        # print "you win to console
        print(" You win!")
        #  quit program
        pygame.quit()

    # if the number of times you swat = the number of times the bee collides with
    # grass patches
    if g_count == 3 and count == 3:
        # quit the game
        pygame.quit()

    pygame.display.update()
