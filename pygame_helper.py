"""
pygame_helper.py
CS 140-02 Fall 2020

This file contains helpful functions for using pygame in class

===========
Changelog:

Version 2020-09-06: initial version
"""

def wait_for_click():
    """
    Pause the program until the user clicks on the pygame window
    :return: None
    """
    import pygame
    print("Waiting for click")
    done = False
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                done = True
        pygame.time.wait(100)

def wait_for_quit():
    """
    Wait until the user quits (closes the pygame window)
    :return: None
    """
    import pygame
    print("Waiting for quit")
    done = False
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True
        pygame.time.wait(100)