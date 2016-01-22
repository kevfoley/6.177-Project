import pygame
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


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.draw.line(screen, (255,255,255), (100, 100), (100, 400), 50)
pygame.draw.line(screen, (255, 255, 255), (151, 100), (151,400), 50)
pygame.display.flip()

pygame.time.wait(5000)
pygame.quit()
