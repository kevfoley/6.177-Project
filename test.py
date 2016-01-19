import pygame

pygame.init()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
#above gets the screen resolution of screen being used, must be done before pygame.display.set_mode()
#screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, 32)

screen = pygame.display.set_mode((500,100))

s = raw_input('')

