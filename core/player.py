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
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed * dt
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_speed
            self.on_ground = False


    def apply_gravity(self, dt):
        if not self.on_ground:
            self.vel_y += 1000 * dt
            self.rect.y += self.vel_y * dt


    def update(self, dt):
        self.handle_input(dt)
        self.apply_gravity(dt)


    def draw(self, screen):
        pygame.draw.rect(screen, RED_COLOR, self.rect)