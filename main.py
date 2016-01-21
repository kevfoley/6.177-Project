import pygame
import os
import random

WIDTH = 10
HEIGHT = 10
directions = [(0,1),(0,-1),(1,0),(0,-1)] #toward (row, col)
# Corresponds to ["East", "West", "South", "North"]

### CHRISTINE ###
class Arena:
    # To be full screen and should have a border
    def __init__(self, x, y, border_width, border_size, food):
        self.x = x
        self.y = y
        self.border_width = border_width
        self.border_size = border_size # tuple of (row, col)
        self.snakes = self.initialize_snakes(10, ((255,0,0), (0,255,0)))
        for snake in self.snakes:
            for part in snake.body_parts:
                print part.row, part.col
        self.food = food
        self.components = pygame.sprite.RenderPlain()
        for snake in self.snakes:
            for parts in snake.body_parts:
                self.components.add(parts)
        for f in self.food:
            self.components.add(f)

    def initialize_snakes(self, length, colors):
        snakes = []
        for i in xrange(len(colors)):
            start_row = self.border_size[0] * directions[i][1] / 2
            start_col = self.border_size[1] * directions[i][0] / 2
            if start_row < 0:
                start_row = start_row*-1
                start_col = self.border_size[1] - 1
            elif start_col < 0:
                start_row = self.border_size[0] - 1
                start_col = start_col * -1
            parts = []
            for j in reversed(range(length)):
                row_n = start_row + j*directions[i][0]
                col_n = start_col + j*directions[i][1]
                b = Body(self, row_n, col_n, colors[i])
                parts.append(b)
            s = Snake(parts)
            snakes.append(s)
        return snakes

    def make_food(self):
        temp_row = random.randrange(self.border_size[0])
        temp_col = random.randrange(self.border_size[1])
        while self.components.has(Body(tempx, tempy)):
            temp_row = random.randrange(self.border_size[0])
            temp_col = random.randrange(self.border_size[1])
        new_food = Body(tempx, tempy)
        self.food.append(new_food)
        self.components.add(new_food)

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
                part.update()

    """
    Checks each snake to see if it has eaten food or collided with another snake or the boundary
    Returns the Snake that loses or None if the game continues
    """

    def detect_collisions(self):
        for snake in self.snakes:
            head = snake.body_parts[0]
            if self.did_collide(head, self.food):
                self.eat_food(snake, self.food)
            if self.check_boundary(head):
                return snake
            for snake in self.snakes:
                if self.did_collide(head, snake.body_parts):
                    return snake
        return None

    def eat_food(self, snake, food):
        snake.add_unit()
        #remove food
        self.make_food()

    """
    Receives a Body object (head) and a list of Body objects (other)
    Returns true is any of the Body objects in the list are at the same position as head and false otherwise
    """
    def did_collide(self, head, other):
        for part in other:
            if head.__eq__(part) and head != part:
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


class Body(pygame.sprite.Sprite):
    def __init__(self,arena, row, col, color):
        pygame.sprite.Sprite.__init__(self)
        self.row = row
        self.col = col
        self.arena = arena
        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = self.arena.get_col_left_loc(col)
        self.rect.y = self.arena.get_row_top_loc(row)
        self.color = color

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def get_loc(self):
        return (self.row, self.col)

    def update(self):
        self.rect.x = self.arena.get_col_left_loc(self.col)
        self.rect.y = self.arena.get_row_top_loc(self.row)

    pass

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
    def __init__(self):
        """
        Set up the components to start a game
        """
        size = (75,75)
        pygame.init()

        width = pygame.display.Info().current_w
        height = pygame.display.Info().current_h
        #above gets the screen resolution of screen being used, must be done before pygame.display.set_mode()
        screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, 32)

        pygame.display.set_caption("Snake")
        food = []
        arena = Arena(10,10, 10, size, food)

        clock = pygame.time.Clock()
        self.main_loop(screen, arena, clock)

    def main_loop(self, screen, arena, clock):
        stop = False
        while stop == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # user clicks close
                    stop = True
                    pygame.quit()
            if stop == False:
                arena.components.draw(screen)
                arena.draw_border(screen, (255,255,255))
                pygame.display.flip()
                arena.move_snakes((directions[0],directions[1]))
                pygame.display.flip()
                loser = arena.detect_collisions()
                ##if loser != None:
                ##    stop = True

        pygame.quit()



class Single_Player(Game):
    pass


class Multi_Player(Game):
    pass

game  = Game()
