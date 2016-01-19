import pygame
import os
import random


WIDTH = 10
HEIGHT = 10

### CHRISTINE ###
class Arena:
    #To be full screen and should have a border
    def __init__(self, x, y, border_width, border_size, snakes, food):
        self.x = x
        self.y = y
        self.border_width = border_width
        self.border_size = border_size
        self.snakes = snakes
        self.food = food
        self.components = pygame.sprite.RenderPlain()
        for snake in self.snakes:
            for parts in snake.body_parts:
                self.components.add(parts)
        for f in self.food:
            self.components.add(f)
        """
        We need to add the snake bodies to the components
        object so that they will be painted on the screen.
        """
        pass

    """
    still working on this
    def make_food(self):
        while len(self.food) < 4:
            random.randrange(self.border_size[0])
            random.randrange(self.border_size[1])
        return

        pass
    """

    def move_snakes(self, directions):
        for snake, dir in self.snakes, directions:
            temp = snake.body_parts[:]
            for part in snake.body_parts:
                if snake.isHead(part):
                    part.row += dir[0]
                    part.col += dir[1]
                else:
                    previous = temp.pop(0)
                    part.row = previous.row
                    part.col = previous.col
        return

    """
    Checks each snake to see if it has eaten food or collided with another snake or the boundary
    Returns the Snake that loses or None if the game continues
    """
    def detect_collisions(self):
        for snake in self.snakes:
            head = snake.body_parts[0]
            if self.did_collide(head, self.food):
                snake.eat_food(self.food)
            for other in self.snakes:
                if not (snake.__eq__(other)):
                    if self.did_collide(head, other) or self.check_boundary(head):
                        return snake
        return None

    """
    Receives a Body object (head) and a list of Body objects (other)
    Returns true is any of the Body objects in the list are at the same position as head and false otherwise
    """
    def did_collide(self, head, other):
        for part in other:
            if head.__eq__(part):
                return True
        return False

    """
    Receives a Body object representing the head of a Snake
    Returns true if the head is out of bounds of the Arena (i.e. if the Snake has hit the wall) and false otherwise
    """
    def check_boundary(self, head):
        max_rows = self.border_size[0]
        max_cols = self.border_size[1]
        return head.row < 0 or head.row > max_rows or head.col < 0 or head.col > max_cols

    def get_col_left_loc(self, col, width = WIDTH):
        return self.x + self.border_width + col*width
        pass

    def get_row_top_loc(self, row, height = HEIGHT):
        return self.y + self.border_width + row*height
        pass

    def draw_border(self, screen, color):
        mid = self.border_width/2
        width = self.border_size[0] * WIDTH
        height = self.border_size[1] * HEIGHT
        pygame.draw.line(screen, color, (self.x-mid, self.y), (width, self.y), self.border_width)
        pygame.draw.line(screen, color, (self.x, self.y-mid), (self.x, height), self.border_width)
        pygame.draw.line(screen, color, (self.x-mid,  height), (width, height), self.border_width)
        pygame.draw.line(screen, color, (width, self.y-mid), (width, height+mid), self.border_width)
        return
    pass

### ROUDI ###
class Body(pygame.sprite.Sprite):
    def __init__(self, row, col, color):
        pygame.sprite.Sprite.__init__(self)
        self.row = row
        self.col = col
        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(color)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    pass

### ROUDI ###
class Snake:
    def __init__(self, body_parts):
        self.body_parts = body_parts

    def is_head(self, part):
        return self.body_parts[0] == part

    def __eq__(self, other):
        return self.body_parts == other.body_parts

    """
    Receives the list of food (as Body objects) in the Arena
    Adds another unit to end of snake and removes the food eaten from food list
    """
    def eat_food(self, food):
      pass


"""
IF WE HAVE TIME

class AI(Snake):
    pass
"""

### KEVIN ###
class Game():
    def __init__():
        pass

    def new_game():
        pass

    def initialize_snakes():
        pass

    def main_loop(screen, arena, clock):

        pass

    pass

class Single_Player(Game):
    pass

class Multi_Player(Game):
    pass

