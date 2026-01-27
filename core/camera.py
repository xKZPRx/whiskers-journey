import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, ZOOM


class Camera:
    def __init__(self, level_width, level_height):
        self.x = 0
        self.y = 0
        self.zoom = ZOOM
        self.level_width = level_width
        self.level_height = level_height


    def update(self, target_rect):
        target_x = target_rect.centerx - WINDOW_WIDTH // 2 / self.zoom
        target_y = target_rect.centery - WINDOW_HEIGHT // 2 / self.zoom

        self.x += (target_x - self.x) * 0.1
        self.y += (target_y - self.y) * 0.1

        max_x = self.level_width - WINDOW_WIDTH / self.zoom
        max_y = self.level_height - WINDOW_HEIGHT / self.zoom

        self.x = max(0, min(self.x, max_x))
        self.y = max(0, min(self.y, max_y))


    def apply(self, rect):
        x = (rect.x - self.x) * self.zoom
        y = (rect.y - self.y) * self.zoom
        width = rect.width * self.zoom
        height = rect.height * self.zoom

        return pygame.Rect(x, y, width, height)