import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, ZOOM


class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.zoom = ZOOM


    def update(self, target_rect):
        target_x = target_rect.centerx - WINDOW_WIDTH // 2 / self.zoom
        target_y = target_rect.centery - WINDOW_HEIGHT // 2 / self.zoom

        self.x += (target_x - self.x) * 0.1
        self.y += (target_y - self.y) * 0.1


    def apply(self, rect):
        x = (rect.x - self.x) * self.zoom
        y = (rect.y - self.y) * self.zoom
        width = rect.width * self.zoom
        height = rect.height * self.zoom

        return pygame.Rect(x, y, width, height)