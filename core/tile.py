import pygame
from settings import TILE_SIZE, WHITE_COLOR


class Tile:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.solid = True

    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE_COLOR, self.rect)