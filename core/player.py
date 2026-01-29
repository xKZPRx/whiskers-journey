import pygame
from settings import TILE_SIZE, PLAYER_SPEED, PLAYER_JUMP_SPEED, RED_COLOR


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.pos_x = float(x)
        self.pos_y = float(y)
        self.vel_x = 0
        self.vel_y = 0
        self.speed = PLAYER_SPEED
        self.jump_speed = PLAYER_JUMP_SPEED
        self.on_ground = False

        self.fishes = 0
        self.has_key = False


    def handle_input(self):
        self.vel_x = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.vel_x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.vel_x += self.speed
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_speed
            self.on_ground = False


    def apply_gravity(self, dt):
        self.vel_y += 1000 * dt


    def collect_fish(self):
        self.fishes += 1


    def collect_key(self):
        self.has_key = True


    def update(self, dt):
        self.prev_rect = self.rect.copy()
        self.handle_input()
        self.apply_gravity(dt)

        self.pos_x += self.vel_x * dt
        self.pos_y += self.vel_y * dt

        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)


    def draw(self, screen, camera):
        draw_rect = camera.apply(self.rect)
        pygame.draw.rect(screen, RED_COLOR, draw_rect)