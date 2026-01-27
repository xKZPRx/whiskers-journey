import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, BLACK_COLOR
from core.level import Level
from core.camera import Camera


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Whisker's Journey")
        
        self.clock = pygame.time.Clock()

        self.running = True
        self.level_index = 1

        self.load_resources()


    def load_resources(self):
        self.level = Level(self.level_index)
        self.camera = Camera()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def handle_collisions(self):
        player = self.level.player
        self.level.player.on_ground = False

        for tile in self.level.tiles:
            if player.rect.colliderect(tile.rect):

                if player.prev_rect.bottom <= tile.rect.top:
                    player.rect.bottom = tile.rect.top
                    player.vel_y = 0
                    player.on_ground = True

                elif player.prev_rect.top >= tile.rect.bottom:
                    player.rect.top = tile.rect.bottom
                    player.vel_y = 0

                elif player.prev_rect.left >= tile.rect.right:
                    player.rect.left = tile.rect.right 
                    player.vel_x = 0

                elif player.prev_rect.right <= tile.rect.left:
                    player.rect.right = tile.rect.left
                    player.vel_x = 0


    def update(self):
        self.dt = self.clock.tick(FPS) / 1000

        self.level.player.update(self.dt)
        self.camera.update(self.level.player.rect)
        self.handle_collisions()


    def draw(self):
        self.screen.fill(BLACK_COLOR)
        self.level.draw(self.screen, self.camera)
        self.level.player.draw(self.screen, self.camera)

        pygame.display.flip()


    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()