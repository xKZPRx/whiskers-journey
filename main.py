import pygame
import traceback
import logging
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, BLACK_COLOR
from core.level import Level
from core.camera import Camera


logging.basicConfig(filename='error.log', level=logging.ERROR)


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

        if not self.level.loaded:
            self.running = False
            return

        self.camera = Camera(self.level.width, self.level.height)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def handle_collisions(self):
        player = self.level.player
        player.on_ground = False

        for tile in self.level.tiles:
            if player.rect.colliderect(tile.rect) and tile.solid:

                if player.prev_rect.bottom <= tile.rect.top:
                    player.pos_y = tile.rect.top - player.rect.height
                    player.vel_y = 0
                    player.on_ground = True
                    player.rect.y = int(player.pos_y)

                if player.prev_rect.top >= tile.rect.bottom:
                    player.pos_y = tile.rect.bottom
                    player.vel_y = 0
                    player.rect.y = int(player.pos_y)

                if player.prev_rect.right <= tile.rect.left:
                    player.pos_x = tile.rect.left - player.rect.width
                    player.rect.x = int(player.pos_x)

                if player.prev_rect.left >= tile.rect.right:
                    player.pos_x = tile.rect.right
                    player.rect.x = int(player.pos_x)

        if player.pos_x <= 0:
            player.pos_x = 0

        if player.pos_x >= self.level.width - player.rect.width:
            player.pos_x = self.level.width - player.rect.width
            
        if player.pos_y <= 0:
            player.pos_y = 0
            player.vel_y = 0

        player.rect.x = int(player.pos_x)
        player.rect.y = int(player.pos_y)


    def update(self):
        self.dt = self.clock.tick(FPS) / 1000

        self.level.player.update(self.dt)
        if self.level.update():
            self.level_index += 1
            self.load_resources()
            return

        self.camera.update(self.level.player.rect)
        self.handle_collisions()


    def draw(self):
        self.screen.fill(BLACK_COLOR)
        self.level.draw(self.screen, self.camera)
        self.level.player.draw(self.screen, self.camera)

        pygame.display.flip()


    def run(self):
        while self.running:
            try:
                self.handle_events()

                if not self.running:
                    break

                self.update()

                if not self.running:
                    break

                self.draw()
            except Exception as e:
                print("An error occured!")
                traceback.print_exc()
                logging.error("An error occurred:\n%s", traceback.format_exc())
                self.running = False


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()