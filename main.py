import pygame
import os
import random

WIDTH = 10
HEIGHT = 10


### CHRISTINE ###
class Arena:
    # To be full screen and should have a border
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


    def make_food(self):
        tempx = random.randrange(self.border_size[0])
        tempy = random.randrange(self.border_size[1])
        while self.components.has(Body(tempx, tempy)):
            tempx = random.randrange(self.border_size[0])
            tempy = random.randrange(self.border_size[1])
        new_food = Body(tempx, tempy)
        self.food.append(new_food)
        self.components.add(new_food)
        return

        pass

    def move_snakes(self, directions):
        for i in range(len(self.snakes)):
            snake = self.snakes[i]
            direction = directions[i]
            temp = snake.body_parts[:]
            for part in snake.body_parts:
                if snake.is_head(part):
                    part.row += direction[0]
                    part.col += direction[1]
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
                self.eat_food(snake, self.food)
            for other in self.snakes:
                if not (snake.__eq__(other)):
                    if self.did_collide(head, other) or self.check_boundary(head):
                        return snake
        return None

    """
    Receives a Body object (head) and a list of Body objects (other)
    Returns true is any of the Body objects in the list are at the same position as head and false otherwise
    """

    def eat_food(self, snake, food):
        snake.add_unit()
        #remove food
        self.make_food()
        return

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

    def get_col_left_loc(self, col, width=WIDTH):
        return self.x + self.border_width + col * width
        pass

    def get_row_top_loc(self, row, height=HEIGHT):
        return self.y + self.border_width + row * height
        pass

    def draw_border(self, screen, color):
        mid = self.border_width / 2
        width = self.border_size[0] * WIDTH
        height = self.border_size[1] * HEIGHT
        pygame.draw.line(screen, color, (self.x - mid, self.y), (width + mid, self.y), self.border_width)
        pygame.draw.line(screen, color, (self.x, self.y - mid), (self.x, height + mid), self.border_width)
        pygame.draw.line(screen, color, (self.x - mid, height), (width + mid, height), self.border_width)
        pygame.draw.line(screen, color, (width, self.y - mid), (width, height + mid), self.border_width)
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
        self.rect = self.image.get_rect()
        #self.rect.x = get_col_left_loc(col)
        #self.rect.y = get_row_top_loc(row)
        self.color = color

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def get_loc(self):
        return (self.row, self.col)

    pass


### ROUDI ###
class Snake:
    def __init__(self, body_parts):
        self.body_parts = body_parts

    def is_head(self, part):
        return self.body_parts[0] == part

    def __eq__(self, other):
        return self.body_parts == other.body_parts

    """adds to body part to end of Snake"""
    def add_unit(self):
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

