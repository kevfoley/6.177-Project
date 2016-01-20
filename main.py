import pygame
import os
import random


WIDTH = 10
HEIGHT = 10

### CHRISTINE ###
class Arena():
    #To be full screen and should have a border
    def __init__(self, x, y, border_width, snakes, food):
        self.x = x
        self.y = y
        self.border_width = border_width
        self.snakes = snakes
        self.food = food
        self.components = pygame.sprite.renderPlain()
        """
        We need to add the snake bodies to the components
        object so that they will be painted on the screen.
        """
        pass

    def make_food():
        # randomly place some food
        pass

    def move_snakes(directions):
        pass

    def detect_collisions():
        pass

    def get_col_left_loc(col, width = WIDTH):
        return x + self.border_width + col*width
        pass

    def get_row_top_loc(row, height = HEIGHT):
        return y + self.border_width + row*height
        pass

    def draw_border():
        pass
    pass

### ROUDI ###
class Body(pygame.sprite.Sprite):
    def __init__(self, row, col, color):
        pygame.sprite.Sprite.__init__(self)
        self.row = row
        self.col = col
        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(color)

    pass

### KEVIN ###
class Food():
    pass

### ROUDI ###
class Snake():
    pass


"""
IF WE HAVE TIME

class AI(Snake):
    pass
"""

### KEVIN ###
class Game():
    def __init__():
        """
        Set up the components to start a game
        """
        rows = 100
        cols = 100
        pygame.init()

        screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)

        pygame.display.set_caption("Snake")
        snakes = []
        food = []
        arena = Arena(0,0, 10, snakes, food)

        clock = pygame.time.Clock()
        main_loop(screen, arena, clock)

    def initialize_snakes():
        pass

    def main_loop(screen, arena, clock):
        arena.components.draw(screen)
        arena.draw_border()
        pygame.display.flip()


class Single_Player(Game):
    pass

class Multi_Player(Game):
    pass
