import pygame
from settings import TILE_SIZE


class Tile:
    def __init__(self, x, y, color, solid, image=None):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.solid = solid
        self.color = color
        self.image = image

    
    def draw(self, screen, draw_rect):
        if self.image:
            scaled_image = pygame.transform.scale(self.image, (draw_rect.width, draw_rect.height))
            screen.blit(scaled_image, draw_rect)
        else:
            pygame.draw.rect(screen, self.color, draw_rect)