import pygame
from settings import TILE_SIZE, PLAYER_SPEED, PLAYER_JUMP_SPEED, RED_COLOR


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.vel_y = 0
        self.speed = PLAYER_SPEED
        self.jump_speed = PLAYER_JUMP_SPEED
        self.on_ground = False


    def handle_input(self, dt):
        self.vel_x = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.vel_x -= self.speed * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.vel_x += self.speed * dt
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_speed
            self.on_ground = False


    def apply_gravity(self, dt):
        if not self.on_ground:
            self.vel_y += 1000 * dt


    def update(self, dt):
        self.prev_rect = self.rect.copy()
        self.handle_input(dt)
        self.apply_gravity(dt)

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y * dt


    def draw(self, screen):
        pygame.draw.rect(screen, RED_COLOR, self.rect)