import pygame
from main import Arena
"""
pygame.init()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
#above gets the screen resolution of screen being used, must be done before pygame.display.set_mode()
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, 32)

screen = pygame.display.set_mode((500,100))

width = 450
height = 90
color = (0, 255, 255)
border_width = 50
x = 0
y = 0
pygame.draw.line(screen, color, (x, y), (width, y), border_width)
pygame.draw.line(screen, color, (x, y), (x, height), border_width)
pygame.draw.line(screen, color, (x,  height), (width, height), border_width)
pygame.draw.line(screen, color, (width, y), (width, height), border_width)
pygame.display.flip()
"""

def new_game():
    pygame.init()
    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h
    #above gets the screen resolution of screen being used, must be done before pygame.display.set_mode()
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, 32)
    #screen = pygame.display.set_mode((200, 300))
    arena = Arena(50, 25, 20, (width/WIDTH -10, height/HEIGHT - 10), [], [])
    arena.draw_border(screen, (0, 255, 255))
    pygame.display.flip()

    pygame.time.wait(5000)
    pygame.quit()

new_game()