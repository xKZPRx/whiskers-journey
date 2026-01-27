import pygame
from settings import TILE_SIZE


class Tile:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.solid = True
        self.color = color

    
    def draw(self, screen, draw_rect):
        pygame.draw.rect(screen, self.color, draw_rect)