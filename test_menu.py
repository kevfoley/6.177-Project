import pygame
import sys
from pygame.locals import *

white = (255,255,255)
black = (0,0,0)


class Pane(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 50)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((1000,500), 0, 32)
        self.screen.fill((white))
        self.x = self.screen.get_rect().centerx - 250
        self.y = self.screen.get_rect().centery - 200
        pygame.display.update()


    def addRect(self):
        self.rect = pygame.draw.rect(self.screen, (black), (self.x, self.y, 500, 400), 0)
        pygame.display.update()

    def addText(self):
        self.screen.blit(self.font.render('Hello!', True, (255,0,0)), (200, 100))
        self.screen.blit(self.font.render("gooe", True, (0,0,255)), (200, 1))
        pygame.display.update()

if __name__ == '__main__':
    Pan3 = Pane()
    Pan3.addRect()
    Pan3.addText()
    for font in pygame.font.get_fonts():
        print font
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();